import json
import os

from django.conf import settings
from django.core.management import BaseCommand


from data.models import Character, Weapon

DATA_DIR = os.path.dirname(settings.BASE_DIR) + '/data/'


class Command(BaseCommand):

    def handle(self, *args, **options) -> None:
        with open(DATA_DIR + 'character_data.json') as f:
            json_file = f.read()
            file_dict = json.loads(json_file)
            for char_data in file_dict:
                print(f"Processing data: {char_data['name']}")
                try:
                    Character.objects.get_or_create(**char_data)
                    print('Success!')
                except Exception as e:
                    print(f"Something went wrong: {e}")

        with open(DATA_DIR + 'weapon_data.json') as f:
            json_file = f.read()
            file_dict = json.loads(json_file)
            for weapon_data in file_dict:
                print(f"Processing data: {weapon_data['name']}")
                try:
                    Weapon.objects.get_or_create(**weapon_data)
                    print('Success!')
                except Exception as e:
                    print(f"Something went wrong: {e}")
