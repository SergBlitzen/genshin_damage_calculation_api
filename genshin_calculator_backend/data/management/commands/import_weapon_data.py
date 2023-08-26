import json
import requests
import re
import time
import random

from typing import Dict, List
from bs4 import BeautifulSoup

from django.core.management import BaseCommand

from data.models import Weapon
from genshin_calculator.settings import env_loader


class Command(BaseCommand):

    def handle(self, *args, **options):
        """
        Main handler for import page data.
        """

        # Loading urls from environment.
        urls: List[str] = [
            env_loader.sword_url,
            env_loader.claymore_url,
            env_loader.polearm_url,
            env_loader.bow_url,
            env_loader.catalyst_url
        ]

        start = time.time()

        # Initiating main url array.
        weapon_urls = []

        for weapon_type_url in urls:
            for url in get_weapon_urls(weapon_type_url):
                weapon_urls.append(url)

        # Parsing data from each url and uploading to database.
        for weapon_url in weapon_urls:
            weapon_data = get_weapon_data(weapon_url)
            for key, value in weapon_data.items():
                # Dictionaries stored as JSONs.
                if isinstance(value, dict):
                    weapon_data[key] = json.dumps(value)
            try:
                Weapon.objects.get_or_create(**weapon_data)
                self.stdout.write(f"Added weapon data: {weapon_data['name']}")
            except Exception as e:
                self.stdout.write(f"Failed to add weapon data: {weapon_data['name']}"
                                  f"Error: {e}")
            time.sleep(1 + (random.randint(1, 100) / 100))

        end = time.time()
        self.stdout.write(f"Data import complete. Time elapsed: {round(end - start)}")


def get_weapon_urls(pages_url: str) -> List[str]:
    """
    Get distinct weapon url from weapon type page.
    """

    # Loading url from environment.
    main_url = env_loader.main_url
    url = pages_url

    # Requesting and parsing page.
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    # Main data stored within JS code as large list, there is
    # regular expression match for finding needed data.
    weapons = soup.find(string=re.compile(env_loader.main_data))

    # Initiating final urls array.
    weapon_urls = []
    weapon_elements = env_loader.weapon_elem_number

    # Parsing data from one big string of stored data.
    for i in range(len(weapons)):
        if weapons[i] == '[':
            start_index = i + weapon_elements
            continue
        if weapons[i] == '>' and start_index:
            end_index = i - 2
            weapon_url = main_url + "".join(weapons[start_index:end_index].split('\\'))
            weapon_urls.append(weapon_url)
            start_index = None
            continue

    return weapon_urls


def get_weapon_data(url) -> Dict[str, str | Dict[str, str]]:
    """
    Parses data from weapon page.

    :param str url: Url of distinct weapon page.
    :return dict: Dictionary with complete data.
    """

    # Initializing main dict.
    weapon_data: Dict[str | Dict[str, str]] = dict()

    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')

    # Getting element with needed info data. All info is written in tables,
    # so next code works with table elements (but still can be customized).
    main_info = soup.find(class_=env_loader.main_class).find_all(env_loader.main_elem)

    # Filling info data with elements. Short name uses lowercase
    # name with stripped symbols.
    weapon_data['name'] = main_info[2].text
    weapon_data['short_name'] = weapon_data['name']
    weapon_data['short_name'].lower().replace(' ', '').replace("'", '')
    weapon_data['type'] = main_info[4].text.split(' ')[-1].lower()

    # Getting element with needed stat data. Each element is a table row.
    weapon_stats = soup.find(class_=env_loader.stat_class).find_all(env_loader.second_elem)
    # Check in case of substat absense.
    try:
        weapon_data['substat_name'] = weapon_stats.pop(0).find_all(env_loader.main_elem)[2].text[6:].lower()
    except IndexError:
        weapon_data['substat_name'] = None

    # List of levels to stitch stats to.
    levels = []
    for elem in weapon_stats:
        levels.append(elem.find_all(env_loader.main_elem)[0].text)

    # Initializing stat lists.
    weapon_atk = []
    weapon_sub = []

    # Getting stats from table elements.
    for i in range(len(weapon_stats)):
        elem_stats = weapon_stats[i].find_all(env_loader.main_elem)
        weapon_atk.append(elem_stats[1].text)
        # Check in case of absense of substat.
        try:
            weapon_sub.append(elem_stats[2].text)
        except IndexError:
            weapon_sub.append(None)

    # Stitching elements with according levels.
    weapon_data['atk'] = dict(zip(levels, weapon_atk))
    weapon_data['substat_lv'] = dict(zip(levels, weapon_sub))

    return weapon_data
