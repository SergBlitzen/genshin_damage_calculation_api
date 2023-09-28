import requests
import re
import time
import random

from typing import Dict, List, Union
from bs4 import BeautifulSoup, ResultSet

from django.core.management import BaseCommand

from data.models import Character, CharHP, CharAtk, CharDef, AscensionStat, CharNormAtk, CharSkill, CharBurst, Move
from genshin_calculator.settings import env_loader


class Command(BaseCommand):

    def handle(self, *args, **options) -> None:
        """
        Main handler for import page data.
        """

        start = time.time()
        main_url = env_loader.character_urls
        urls = get_character_urls(main_url)
        self.stdout.write("Got character URLs!")
        self.stdout.write("Starting to get characters data...")

        for url in urls:
            character_data = get_character_data(url)
            self.stdout.write(f"Got character data: {character_data['name']}!")

            try:
                character = Character.objects.create(
                    name=character_data['name'],
                    short_name=character_data['short_name'],
                    weapon=character_data['weapon'],
                    element=character_data['element'],
                    ascension_name=character_data['ascension_stat']
                )
                CharHP.objects.create(
                    character=character,
                    **character_data['hp']
                )
                CharAtk.objects.create(
                    character=character,
                    **character_data['atk']
                )
                CharDef.objects.create(
                    character=character,
                    **character_data['defense']
                )
                AscensionStat.objects.create(
                    character=character,
                    **character_data['ascension']
                )

                char_moves = {
                    'normal_atk': CharNormAtk,
                    'skill': CharSkill,
                    'burst': CharBurst
                }

                for skill_name, model in char_moves.items():
                    skill = model.objects.create(
                        character=character
                    )
                    for name, stat in character_data[skill_name].items():
                        move_obj = Move.objects.create(
                            name=name,
                            **stat
                        )
                        skill.moves.add(move_obj)
            except Exception as e:
                self.stdout.write(
                    f"Error while processing character {character_data['name']}."
                    f"Text: {e}"
                )

            time.sleep(1 + (random.randint(1, 100) / 100))

        end = time.time()
        self.stdout.write(f"Data import complete. Time elapsed: {round(end - start)}")


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
    char_data: str = env_loader.main_data
    chars = soup.find(text=re.compile(char_data))
    start_char_index: int = env_loader.start_char_index
    end_char_index: int = env_loader.end_char_index
    chars: str = str(chars[start_char_index:end_char_index])

    # Main loop for getting all URLs. As data is stored in
    # separate arrays, URLs are found in the beginning
    # of each array and parsed by simple string slicing.
    start_index: Union[int, None] = None
    start_slice_index: int = env_loader.character_elem_number
    url: str = env_loader.main_url
    for i in range(0, len(chars)):
        if chars[i] == '[':
            start_index = i + start_slice_index
            continue
        if chars[i] == '>' and start_index:
            end_index = i - 2
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
    main_elem = env_loader.main_elem

    # Parsing is divided by functions.
    soup = BeautifulSoup(request_data, "html.parser")

    main_info_class: str = env_loader.main_class
    main_info = soup.find(class_=main_info_class).find_all(main_elem)
    get_main_info(main_info, char_data)

    main_stats_class: str = env_loader.stat_class
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
        # Elemental burst table.
        burst = main_skills[3]
    else:
        burst = main_skills[2]
    get_character_skills(burst, char_data, skill_type='burst')

    return char_data


def get_main_info(char_page: ResultSet, char_data: Dict) -> None:
    """
    Function that fills main data dictionary with character info.

    :param ResultSet char_page: Parsed data of main character info.
    :param char_data: Dictionary of current character data.
    :return None: None.
    """

    name = char_page[2].text
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
    main_elem: str = env_loader.main_elem
    second_elem: str = env_loader.second_elem
    stats_names = char_page.find(second_elem).find_all(main_elem)[:7]
    for name in stats_names:
        # "Bonus" means ascension stat.
        if 'Bonus' in name.text:
            char_data['ascension'] = {}
        # Preventing future conflicts with Python syntax.
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
            lv = 'lv' + row[0].text.lower().replace('+', 'plus')
            if 'Bonus' in j.text:
                # Each iteration fills the current level values.
                # Num coordinates needed stat name index and row element.
                char_data['ascension'][lv] = stat.find_all("td")[num].text
                ascension = j.text[6:]
                char_data['ascension_stat'] = ascension.replace('%', '')
            elif 'Def' in j.text:
                char_data['defense'][lv] = stat.find_all("td")[num].text
            else:
                char_data[j.text.lower().replace('%', '')][lv] = stat.find_all("td")[num].text
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
    main_elem: str = env_loader.main_elem
    second_elem: str = env_loader.second_elem
    dmg_class: str = env_loader.character_dmg_class

    skill_rows = skill_table.find(class_=dmg_class).find(second_elem).find_all(main_elem)

    # As there are exact number of elements in each row and page parses wrong
    # without closing tags, stats can be parsed as slices.
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
    for i in range(len(levels)):
        levels[i] = levels[i].lower()

    # Parsing normal atk stats. First element in row is a stat name,
    # and the rest of data are stripped from tags and zipped with levels
    # list into dictionary with same name.
    for stat in skill_list:
        stat_name = stat[0].text.lower().replace('-', '_').replace('%', '_').replace('/', '_').replace(' ', '_')
        # Adding short character name to skill name for easy identifying.
        stat_name = char_data['short_name'] + '_' + stat_name
        stat_dmg_levels = []
        for dmg_percent in stat[1:]:
            stat_dmg_levels.append(dmg_percent.text)
        stat_dict = dict(zip(levels, stat_dmg_levels))
        char_data[skill_type][stat_name] = stat_dict
    return None
