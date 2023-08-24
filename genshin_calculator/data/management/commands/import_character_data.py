import json
import os

import requests
import re
import time
import random

from typing import Dict, List, Union
from bs4 import BeautifulSoup, ResultSet

from django.core.management import BaseCommand

from data.models import Character
from genshin_calculator.settings import env_loader


class Command(BaseCommand):

    def handle(self, *args, **options) -> None:
        """
        Main handler for import page data.
        """
        main_url = env_loader.character_urls
        urls = get_character_urls(main_url)
        self.stdout.write("Got character URLs!")
        self.stdout.write("Starting to get characters data...")
        start = time.time()

        for url in urls:
            character_data = get_character_data(url)
            for key, value in character_data.items():
                if isinstance(value, dict):
                    character_data[key] = json.dumps(value)
            character_data.pop('lv')
            try:
                Character.objects.get_or_create(**character_data)
                self.stdout.write(f"Added character data: {character_data['name']}")
            except Exception as e:
                self.stdout.write(f"Failed to add character data: {character_data['name']}."
                                  f"Error: {e}")
            time.sleep(1 + (random.randint(1, 100) / 100))

        end = time.time()
        self.stdout.write(f"Data import complete. Time elapsed: {end - start}")


def get_character_urls(pages_url: str) -> List[str]:
    """
    Function to get list of all character URLs.

    :param str pages_url: URL of characters page.
    :return: List of character URLs.
    """
    char_urls: List[str] = []

    request = requests.get(pages_url)
    request_data = request.text

    # Needed data is stored within JS code and BS object
    # cannot process it fully, so there is some manual
    # processing to get data.
    soup = BeautifulSoup(request_data, "html.parser")
    char_data: str = env_loader.char_data
    chars = soup.find(text=re.compile(char_data))
    start_char_index: int = env_loader.start_char_ind
    end_char_index: int = env_loader.end_char_ind
    chars: str = str(chars[start_char_index:end_char_index])

    # Main loop for getting all URLs. As data is stored in
    # separate arrays, URLs are found in the beginning
    # of each array and parsed by simple string slicing.
    start_index: Union[int, None] = None
    start_slice_index: int = env_loader.start_url_ind
    end_slice_index: int = env_loader.end_url_ind
    url: str = env_loader.url
    for i in range(0, len(chars)):
        if chars[i] == '[':
            start_index = i + start_slice_index
            continue
        if chars[i] == '>' and start_index:
            end_index = i - end_slice_index
            char_url = url + "".join(chars[start_index:end_index].split('\\'))
            char_urls.append(char_url)
            start_index = None
            continue

    return char_urls


def get_character_data(char_url: str) -> Dict[str, str | Dict[str, str | Dict[str, str]]]:
    """
    Function to get full character data.

    :param str char_url: URL of distinct character.
    :return char_data: Dictionary with full character data.
    """
    char_data: Dict[str, str | Dict[str, str | Dict[str, str]]] = {}

    request = requests.get(char_url)
    request_data = request.text

    # Getting main parsing element.
    main_elem = env_loader.character_main_elem

    # Parsing is divided by functions.
    soup = BeautifulSoup(request_data, "html.parser")

    main_info_class: str = env_loader.character_main_class
    main_info = soup.find(class_=main_info_class).find_all(main_elem)
    get_main_info(main_info, char_data)

    main_stats_class: str = env_loader.character_stat_class
    main_stats = soup.find(class_=main_stats_class)
    get_character_main_stats(main_stats, char_data)

    main_skill_class: str = env_loader.character_skill_class
    main_skills = soup.find_all(class_=main_skill_class)
    normal_atk = main_skills[0]
    get_character_skills(normal_atk, char_data, skill_type='normal_atk')
    skill = main_skills[1]
    get_character_skills(skill, char_data, skill_type='skill')
    # Check for an alternate sprint.
    if all([i.find(class_="genshin_table skill_dmg_table") for i in main_skills[:4]]):
        # Sprint table if character has one.
        sprint = main_skills[2]
        get_character_skills(sprint, char_data, skill_type='sprint')
        # Elemental burst table.
        burst = main_skills[3]
    else:
        burst = main_skills[2]
    get_character_skills(burst, char_data, skill_type='burst')
    print(f"Got character data: {char_data['name']}")

    return char_data


def get_main_info(char_page: ResultSet, char_data: Dict) -> None:
    """
    Function that fills main data dictionary with character info.

    :param ResultSet char_page: Parsed data of main character info.
    :param char_data: Dictionary of current character data.
    :return None: None.
    """

    name = char_page[2].text
    print(f'Processing character: {name}')
    char_data['name'] = name
    short_name = name.lower().replace(' ', '')
    char_data['short_name'] = short_name
    weapon = char_page[12].text.strip().lower()
    char_data['weapon'] = weapon
    element = char_page[14].text.strip().lower()
    char_data['element'] = element
    return None


def get_character_main_stats(char_page: BeautifulSoup, char_data: Dict) -> None:
    """
    Fills dictionary with main stat data.

    :param BeautifulSoup char_page: Set with main stat info.
    :param char_data: Dictionary of current character data.
    :return None: None.
    """

    # Stat names for creating new variable dicts.
    main_elem: str = env_loader.character_main_elem
    second_elem: str = env_loader.character_second_elem
    stats_names = char_page.find(main_elem).find_all(second_elem)[:7]
    for name in stats_names:
        # Replace bonus stat with ascension.
        if 'Bonus' in name.text:
            char_data['ascension'] = {}
        # Replace "def" name with "defense" in order to prevent
        # future conflicts with Python syntax.
        elif 'Def' in name.text:
            char_data['defense'] = {}
        else:
            char_data[name.text.lower().replace('%', '')] = {}

    # Main for loop to fill dicts.
    for stat in char_page.find_all(second_elem)[1:]:
        # Get row of current level stats.
        row = stat.find_all(main_elem)
        # Enumerate names for index access.
        for num, j in enumerate(stats_names):
            if 'Bonus' in j.text:
                # Each iteration fills the current level values.
                # Num coordinates needed stat name index and row element.
                char_data['ascension'][row[0].text.lower()] = stat.find_all("td")[num].text
                ascension = j.text[6:]
                char_data['ascension_stat'] = ascension.replace('%', '')
            elif 'Def' in j.text:
                char_data['defense'][row[0].text.lower()] = stat.find_all("td")[num].text
            else:
                char_data[j.text.lower().replace('%', '')][row[0].text.lower()] = stat.find_all("td")[num].text
    return None


def get_character_skills(skill_table: BeautifulSoup, char_data: Dict, skill_type: str) -> None:
    """
    Processes table and fills data dict with corresponding skill dict.

    :param BeautifulSoup skill_table: Skill table to process.
    :param char_data: Dictionary of current character data.
    :param str skill_type: Skill type for creating dict key.
    :return None: None.
    """

    char_data[skill_type] = {}

    # Getting elements for page parsing.
    main_elem: str = env_loader.character_main_elem
    second_elem: str = env_loader.character_second_elem
    dmg_class: str = env_loader.character_dmg_class

    skill_rows = skill_table.find(class_=dmg_class).find(second_elem).find_all(main_elem)

    # As there are exact number of elements in each row and page parses wrong
    # without closing "tr" tags, stats can be parsed as slices.
    skill_stats_elements: int = int(env_loader.character_stats_elem_number)
    skill_list: list = []
    for _ in range(len(skill_rows) // skill_stats_elements):
        skill_list.append(skill_rows[:skill_stats_elements])
        skill_rows = skill_rows[skill_stats_elements:]

    # Table of skills has different structure with stats displayed in rows
    # instead of columns, so it's better to stitch stats with already done level list,
    # which is in first row.
    # The first element of list in an empty "td" tag.
    levels = list(map(BeautifulSoup.get_text, skill_list[0][1:]))
    skill_list.pop(0)

    # Parsing normal atk stats. First element in row in a stat name,
    # and the rest of data are stripped from tags and zipped with levels
    # list into dictionary with same name.
    for stat in skill_list:
        stat_name = stat[0].text.lower().replace('-', '_').replace('%', '_').replace('/', '_').replace(' ', '_')
        stat_dmg_levels = []
        for dmg_percent in stat[1:]:
            stat_dmg_levels.append(dmg_percent.text)
        stat_dict = dict(zip(levels, stat_dmg_levels))
        char_data[skill_type][stat_name] = stat_dict
    return None
