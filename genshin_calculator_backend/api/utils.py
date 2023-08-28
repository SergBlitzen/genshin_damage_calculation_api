import json

from typing import Dict, Union

from data.models import Character, Weapon


def get_character_stats(
        character: Character
) -> Dict[str, Dict[str, str]]:
    """
    Unloads character data from JSON and returns
    it as a dictionary of stats.

    :param Character character: Character model object.
    :return Dict stats: Data interpreted as dictionary.
    """

    stats = {
        'name': character.name,
        'element': character.element,
        'type': character.weapon,
        'hp': json.loads(character.hp),
        'atk': json.loads(character.atk),
        'defense': json.loads(character.defense),
        'normal_attack': json.loads(character.normal_atk),
        'skill': json.loads(character.skill),
        'burst': json.loads(character.burst),
    }

    return stats


def get_weapon_stats(
        weapon: Weapon
) -> Dict[str, Dict[str, str]]:
    """
    Unloads weapon data from JSON and returns
    it as a dictionary of stats.

    :param Weapon weapon: Weapon model object.
    :return Dict stats: Data interpreted as dictionary.
    """

    stats = {
        'name': weapon.name,
        'type': weapon.type,
        'atk': json.loads(weapon.atk),
        weapon.substat_name: json.loads(weapon.substat_lv)
    }

    return stats

#
# def calculate_skill_damage(
#         character: Character,
#         skill: Dict[str, Dict[str, str]],
#         level: int
# ) -> Dict[str, Dict[str, Union[int, float]]]:
#
#     return ...


def sum_initial_attributes(
        character: Character,
        weapon: Weapon,
        query_params,
) -> Union[str, Dict]:
    """
    Sums initial character and weapon attributes.

    :param Character character: Character object.
    :param Weapon weapon: Weapon object.
    :param Dict query_params: Dictionary of query parameters.

    :return Dict response_data: Initial dictionary of response data.
    """

    if weapon.type != character.weapon:
        return "Selected character cannot wield this weapon!"

    response_data = {}

    character_level = query_params['character_level']
    character_data = get_character_stats(character)
    weapon_level = query_params['weapon_level']
    weapon_data = get_weapon_stats(weapon)

    response_data['character_name'] = character_data['name']
    response_data['element'] = character_data['element']
    response_data['weapon_type'] = character_data['type']
    response_data['weapon'] = weapon_data['name']
    response_data['hp'] = int(character_data['hp'][character_level])
    response_data['atk'] = (float(character_data['atk'][character_level]) +
                            float(weapon_data['atk'][weapon_level]))
    response_data['defense'] = float(
        character_data['defense'][character_level]
    )
    response_data['skills'] = [
        character_data['normal_attack'],
        character_data['skill'],
        character_data['burst']
    ]

    # for skill in response_data['skills']:
    #     for skill_stat in skill.values():
    #         if '%' in skill_stat.split(' ')[-1]:
    #

    return response_data

