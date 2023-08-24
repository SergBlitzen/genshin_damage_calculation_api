import os

from dotenv import load_dotenv

load_dotenv()


class Loader:
    # Django secret key.
    secret_key = os.getenv('SECRET_KEY')

    # Page elements.
    main_url: str = os.getenv('CHAR_LIST_URL')
    url: str = os.getenv('MAIN_URL')
    char_data: str = os.getenv('CHAR_DATA')
    main_class: str = os.getenv('MAIN_CLASS')
    main_elem: str = os.getenv('MAIN_ELEM')
    second_elem: str = os.getenv('SECOND_ELEM')
    stat_class: str = os.getenv('STAT_CLASS')
    skill_class: str = os.getenv('SKILL_CLASS')
    dmg_class: str = os.getenv('DMG_CLASS')
    start_char_ind = int(os.getenv('START_CHAR_IND'))
    end_char_ind = int(os.getenv('END_CHAR_IND'))
    start_url_ind = int(os.getenv('START_URL_IND'))
    end_url_ind = int(os.getenv('END_URL_IND'))
    normal_atk_ind = int(os.getenv('NORMAL_ATK_IND'))
    skill_ind = int(os.getenv('SKILL_IND'))
    skills_border = int(os.getenv('SKILLS_BORDER'))
    sprint_ind = int(os.getenv('SPRINT_IND'))
    burst_ind = int(os.getenv('BURST_IND'))

