# Wiki Actual Version : v1.5.6

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

# README
## Description
This is a web application built using the Django framework in Python, designed to help the Archero gaming community. Archero is a popular game that involves battling through levels while upgrading your character's abilities and equipment. The application offers a range of tools to help players improve their gameplay, including an advanced stats calculator, tier lists, and other useful information.

## Contributors
I am the sole contributor to this project, which was started in late August 2022.

## Technologies
The application is built using a range of technologies, including:

- Python
- JavaScript
- HTML
- CSS
- JSON
- crontab

It also uses Docker for deployment, with a PostgreSQL database.

## Getting Started
To run the application locally, you will need to have Docker installed on your system. Once you have Docker installed, simply clone the repository and run the docker-compose up command to start the application.
Here are the step to run it : 
- Once you've cloned this repository, you will need to change the services.db.volumes path from : path_local_db_data_store to what you want
- Then when you are at the root of the application (in public-archero-wiki-docker> ) you can execute these command :
```bash
cd .\web-project\
docker build -t archero .        
docker-compose up -d --env-file=myenvfile.env
```

## Usage
Once the application is up and running, you can access it by navigating to the appropriate URL in your web browser (localhost:8000 or 0.0.0.0:8000 or 127.0.0.1:8000). From there, you can explore the various features and tools offered by the application to help you improve your gameplay in Archero.

## License
This project is licensed under the MIT License - see the LICENSE file for details.


____
## Naming convention rule for calculation variables :
- type : var (+x%) / flat (+x)
- type2 : passiv / activ
- boost : atk / hp
- system : (jewel, altar, dragon etc...)
- for which variable it serve : (coef1)
- cumul for the total/global
- `[cumul_]system_type_type2_boost_...`

___
# Step change database :

- `python -Xutf8 manage.py dumpdata > data.json`
- `changing models.py`
- `python manage.py makemigrations`
- `python manage.py migrate`
- `if migrate doesn't work, you need to delete the database through the psql command and DROP TABLE`
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py loaddata database_dump.json`
<!-- Remind to fill up the database_dump.json -->
---


```diff
Todo list: 
- export gsheet
- add not allowed ingame_id
```
```diff
Future Release:
- altar_hero_projectile_resistance incrementation data wrong
- login ask if this profile is yours and use it if yes etc...
- security sql injection fix (owasp zap)
- damage calc add new var
- jewel/dragon guide
- make universal name for e.g : "range_dmg_var" or "ranged_dmg_var" ?
- add all heroes star for future information in profile page
- add page for emulator skill in fight with skill you can check (don't forget medals boost)
- details page add run boost from glyphs, dragon, stuff etc...
- translate
- item (especially for ring, get value with dict.get instead of having mythic_boost, titan_tales_boost etc....)
- store cookie in session
- remove space in key of local_data (skill)
- maze soluce display only current week pattern
- relics stat does apply if level, star and exclusive are = to 0
- damage fix with HACKER profile, and also when looking at other profile, because stats doesn't load
```

Update May 29, 2023 6:45 PM