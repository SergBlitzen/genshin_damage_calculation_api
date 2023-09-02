# Genshin Damage Calculator API

Once a backend part of whole project which hasn't launched, now it's a proof-of-concept independent API module for
damage calculation of Genshin characters.<br>
<br>
Calculator features custom data scraping module which could be flexible enough to customise scraping from different
resources while code in actual repo serves only as an example.<br>
<br>

### Stack

Based on:
<br>• Python 3.10
<br>• Django 4.1.4
<br>• Django Rest Framework 3.14.0

Additionally used tools:
<br>• BeautifulSoup4
<br>• Dotenv

## Current state
Implemented database structure: models, serializers and endpoints for data representation. Further features like
filtering and pagination is in progress.
<br>
<br>Base data are represented as dictionaries, so the main feature of database is storing them as JSON's, as there is no
proper way to spread much different data in distinct tables.
<br>
<br>Actual calculation is at early state: there is still no artefact support as well as many more features like passive
stats and abilities. Basic damage calculation is implemented.

## To-do
Tweaking with database as well as implementing more customized models for better calculation process.

## Launching project

### Interpreter settings

As for now, project only uses SQLite DB and launches locally without external tools.
<br>
<br>After cloning repo, install Python virtual env in root:
<br>```python -m venv venv```
<br>Install dependencies:
<br>```pip install -r requirements.txt```

### Environment adjustment
All environment settings is declared in Loader class object in settings.py. 
<br>Adjust data secrets and debug in environment with .env file in genshin_calculator folder with settings.py.
<br>Env file examples:
<br>• SECRET_KEY: str — secret Django key;
<br>• DEBUG: bool — enable debug mode (not for production!)

### Parser adjustments
Parser can (and probably should) be customized for different resources scraping. In example code data is provided
with string of arrays and  rows of tables. Data which requires dictionary representation is stored in database as JSONs.
Check Loader class and model settings for more information.
Env file examples:
<br>• MAIN_URL: str — main resource url which is joined with distinct object id while parsing urls;
<br>• MAIN_DATA: str — in example: JS variable which stored main data for parser. Check parser modules for more info;
<br>• [ITEM]_ELEMENTS_NUMBER: int — in addition to variable above this one used to determine string slicing range;
<br>• MAIN_ELEM: str — HTML code tags for parsing with BeautifulSoup;
<br>• [ITEM]_CLASS: str — HTML code class tag for parsing with BeautifulSoup.
<br>
<br> It is strongly recommended to adjust parser for specific resource, as there is no sample data (for now).

### Importing data
With adjusted parsers, data can be import with management commands:
<br> ```python manage.py import_character_data```
<br> ```python manage.py import_weapon_data```

### Launching server
Launch server with:
<br>```python manage.py runserver```


## How to use
As this is only an API module, usage is limited with accessing endpoints. Preferred tool is Postman.
<br>All endpoints and viewsets are declared in "api" application.
<br>Working endpoints:
<br>• api/v1/characters/{id}
<br>• api/v1/weapons/{id}


## Disclaimer
This project is non-profit and does not support commercial use of any data provided with web scraping means.
<br> Feel free to fork and customize.
<br>
<br> Project done by: Serg Blitzen
<br> github.com/SergBlitzen
