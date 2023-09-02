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
        'def': json.loads(character.defense),
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


def calculate_skill_damage(
        character: Character,
        weapon: Weapon,
        data: Dict[str, Dict[str, str]],
        skill: Dict[str, str],
        level: str
) -> Dict[str, Dict[str, Union[int, float]]]:
    """
    Main calculation function. Processes one skill at a time.

    :param character: Current character.
    :param weapon: Current weapon.
    :param data: Dictionary of current character data.
    :param skill: Current skill data.
    :param level: Skill level
    :return Dict[str, Dict[str, Union[int, float]]]: Dictionary of
    calculated value.
    """

    skill_data = {}

    for move, stats in skill.items():
        stat = stats['Lv' + level]
        # Current implementation of damage skill recognition.
        if '%' in stat:
            split_stat = stat.split(' ')
            print(f"{move} {split_stat}")
            if 'HP' in split_stat:
                damage_stat = data['hp']
            elif 'DEF' in split_stat:
                damage_stat = data['def']
            else:
                damage_stat = data['atk']
            for dmg in split_stat:
                if '%' in dmg:
                    new_dmg = dmg.replace('%', ' ').split(' ')
                    damage = round(float(new_dmg[0]) * damage_stat / 100, 2)
                    if not skill_data.get(move):
                        skill_data[move] = str(damage)
                    else:
                        skill_data[move] += f" + {str(damage)}"
                    skill_data[move] += f"{new_dmg[1]}"
        else:
            if not skill_data.get(move):
                skill_data[move] = stats['Lv' + level]
            else:
                continue

    return skill_data


def get_attributes(
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
    response_data['atk'] = round(
        float(character_data['atk'][character_level]) +
        float(weapon_data['atk'][weapon_level]), 2)
    response_data['def'] = round(
        float(character_data['def'][character_level]), 2)
    skills = {
        'normal_attack': character_data['normal_attack'],
        'skill': character_data['skill'],
        'burst': character_data['burst']
    }
    levels = {
        'normal_attack': query_params['attack_level'],
        'skill': query_params['skill_level'],
        'burst': query_params['burst_level']
    }
    response_data['skills'] = []

    for skill, level in levels.items():
        response_data['skills'].append(calculate_skill_damage(
            character, weapon, response_data, skills[skill], level
        ))

    return response_data

