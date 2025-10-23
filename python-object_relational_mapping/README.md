Python - Object-Relational Mapping (ORM)

Description
This project links two powerful worlds: Databases and Python.
You will first interact with a MySQL database directly using the MySQLdb module,
and then transition into a higher-level abstraction using SQLAlchemy, a popular
Object Relational Mapper (ORM). The goal is to understand both raw SQL queries
and ORM-based data manipulation, where you interact with database tables as
Python objects.

Learning Objectives
- Connect to a MySQL database from Python
- SELECT and INSERT rows from Python
- Understand what an ORM is and how it works
- Map a Python class to a MySQL table using SQLAlchemy
- Perform CRUD operations with ORM syntax

Requirements
- Ubuntu 20.04 LTS, python3 (3.8.5)
- MySQLdb 2.0.x, SQLAlchemy 1.4.x
- Files end with newline, start with #!/usr/bin/python3, executable, pycodestyle 2.7.*
- Docstrings for all modules/classes/functions
- Do NOT use execute() with SQLAlchemy

Installation and Setup
1) MySQL 8.0: sudo apt update && sudo apt install mysql-server
2) MySQLdb: sudo apt-get install python3-dev libmysqlclient-dev zlib1g-dev && sudo pip3 install mysqlclient==2.0.3
3) SQLAlchemy: sudo pip3 install SQLAlchemy==1.4.22

Project Files and Tasks
- 0-select_states.py — list all states (hbtn_0e_0_usa)
- 1-filter_states.py — list states starting with 'N'
- 2-my_filter_states.py — filter by name (NOT injection-safe)
- 3-my_safe_filter_states.py — filter by name (safe/parameterized)
- 4-cities_by_state.py — all cities with state (one execute())
- 5-filter_cities.py — cities of a given state (safe; one execute())
- model_state.py — SQLAlchemy Base + State model
- 6-model_state.py — create states table via metadata
- 7-model_state_fetch_all.py — list all State objects
- 8-model_state_fetch_first.py — first State
- 9-model_state_filter_a.py — states containing 'a'
- 10-model_state_my_get.py — id of State by name or 'Not found'
- 11-model_state_insert.py — insert 'Louisiana' and print id
- 12-model_state_update_id_2.py — rename id=2 to 'New Mexico'
- 13-model_state_delete_a.py — delete states whose name contains 'a'
- model_city.py — City model (id, name, state_id FK)
- 14-model_city_fetch_by_state.py — list City objects with State name

Key Concepts
Without ORM: cur.execute('SELECT * FROM states ORDER BY id ASC')
With ORM: for s in session.query(State).order_by(State.id).all(): print(f'{s.id}: {s.name}')

Examples
$ ./0-select_states.py root root hbtn_0e_0_usa
(1, 'California')
(2, 'Arizona')
(3, 'Texas')
(4, 'New York')
(5, 'Nevada')

$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
4: New York
5: Nevada

Author
Victor E. Díaz — Holberton School Student, Cohort #27 — Foundations v2.1 - Part 2
GitHub: https://github.com/TenDays
