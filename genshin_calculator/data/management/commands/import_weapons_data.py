import json
import requests
import re
import time
import random

from typing import Dict, List, Union
from bs4 import BeautifulSoup, ResultSet

from django.core.management import BaseCommand

from data.models import Weapon
from genshin_calculator.settings import env_loader


class Command(BaseCommand):

    def handle(self, *args, **options):
        urls: List[str] = [
            "https://genshin.honeyhunterworld.com/fam_sword/?lang=EN",
            "https://genshin.honeyhunterworld.com/fam_claymore/?lang=EN",
            "https://genshin.honeyhunterworld.com/fam_polearm/?lang=EN",
            "https://genshin.honeyhunterworld.com/fam_bow/?lang=EN",
            "https://genshin.honeyhunterworld.com/fam_catalyst/?lang=EN"
        ]

        start = time.time()

        for weapon_type_url in urls:
            ...

        weapon_urls = []

        for weapon_url in weapon_urls:
            weapon_data = get_weapon_data(weapon_url)
            for key, value in weapon_data.items():
                if isinstance(value, dict):
                    weapon_data[key] = json.dumps(value)
            weapon_data.pop('lv')
            try:
                Weapon.objects.get_or_create(**weapon_data)
                self.stdout.write(f"Added weapon data: {weapon_data['name']}")
            except Exception as e:
                self.stdout.write(f"Failed to add weapon data: {weapon_data['name']}"
                                  f"Error: {e}")
            time.sleep(1 + (random.randint(1, 100) / 100))

        end = time.time()
        self.stdout.write(f"Data import complete. Time elapsed: {end - start}")


def get_weapon_urls(pages_url: str) -> List[str]:
    pass


def get_weapon_data(url) -> Dict[str, str | Dict[str, str | Dict[str, str]]]:
    pass
