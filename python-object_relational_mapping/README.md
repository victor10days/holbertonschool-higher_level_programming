# Python - Object-relational mapping

This project demonstrates the connection between databases and Python using two different approaches: **MySQLdb** (direct SQL queries) and **SQLAlchemy** (Object Relational Mapper).

## Background Context

In this project, we explore two amazing worlds: Databases and Python!

- **First part**: Using the module `MySQLdb` to connect to a MySQL database and execute SQL queries
- **Second part**: Using the module `SQLAlchemy`, an Object Relational Mapper (ORM)

The biggest difference is: **no more SQL queries!** With an ORM, your biggest concern will be "What can I do with my objects" and not "How this object is stored? where? when?". You won't write any SQL queries only Python code.

## Requirements

- **Editors**: vi, vim, emacs
- **Interpreter**: Ubuntu 20.04 LTS using python3 (version 3.8.5)
- **MySQLdb version**: 2.0.x
- **SQLAlchemy version**: 1.4.x
- All files should end with a new line
- First line of all files should be exactly `#!/usr/bin/python3`
- Code should use the pycodestyle (version 2.7.*)
- All files must be executable
- All modules, classes and functions should have documentation

## Installation

### Install MySQL 8.0
```bash
sudo apt update
sudo apt install mysql-server
mysql --version
```

### Install MySQLdb module version 2.0.x
```bash
sudo apt-get install python3-dev
sudo apt-get install libmysqlclient-dev
sudo apt-get install zlib1g-dev
sudo pip3 install mysqlclient
```

### Install SQLAlchemy module version 1.4.x
```bash
sudo pip3 install SQLAlchemy
```

## Files Description

### MySQLdb Tasks (0-5)
- **0-select_states.py**: Lists all states from the database
- **1-filter_states.py**: Lists all states with a name starting with 'N'
- **2-my_filter_states.py**: Displays all values in states table where name matches the argument (vulnerable to SQL injection)
- **3-my_safe_filter_states.py**: Same as task 2 but safe from MySQL injections
- **4-cities_by_state.py**: Lists all cities from the database with their states
- **5-filter_cities.py**: Lists all cities of a specific state

### SQLAlchemy Tasks (6-14)
- **model_state.py**: Contains the class definition of a State and instance Base
- **6-model_state.py**: Script that creates the State table in database
- **7-model_state_fetch_all.py**: Lists all State objects from the database
- **8-model_state_fetch_first.py**: Prints the first State object from the database
- **9-model_state_filter_a.py**: Lists all State objects that contain the letter 'a'
- **10-model_state_my_get.py**: Prints the State object with the name passed as argument
- **11-model_state_insert.py**: Adds the State object "Louisiana" to the database
- **12-model_state_update_id_2.py**: Changes the name of a State object where id = 2
- **13-model_state_delete_a.py**: Deletes all State objects with a name containing the letter 'a'
- **model_city.py**: Contains the class definition of a City
- **14-model_city_fetch_by_state.py**: Prints all City objects from the database

## Usage Examples

### MySQLdb Examples
```bash
# List all states
./0-select_states.py root root hbtn_0e_0_usa

# Filter states starting with 'N'
./1-filter_states.py root root hbtn_0e_0_usa

# Search for a specific state
./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'

# Safe search for a specific state
./3-my_safe_filter_states.py root root hbtn_0e_0_usa 'Arizona'

# List all cities with their states
./4-cities_by_state.py root root hbtn_0e_4_usa

# List cities of a specific state
./5-filter_cities.py root root hbtn_0e_4_usa Texas
```

### SQLAlchemy Examples
```bash
# List all states using SQLAlchemy
./7-model_state_fetch_all.py root root hbtn_0e_6_usa

# Get first state
./8-model_state_fetch_first.py root root hbtn_0e_6_usa

# Filter states containing 'a'
./9-model_state_filter_a.py root root hbtn_0e_6_usa

# Get state by name
./10-model_state_my_get.py root root hbtn_0e_6_usa Texas

# Add new state
./11-model_state_insert.py root root hbtn_0e_6_usa

# Update state
./12-model_state_update_id_2.py root root hbtn_0e_6_usa

# Delete states containing 'a'
./13-model_state_delete_a.py root root hbtn_0e_6_usa

# List cities with states
./14-model_city_fetch_by_state.py root root hbtn_0e_14_usa
```

## Learning Objectives

By the end of this project, you should be able to explain:

- How to connect to a MySQL database from a Python script
- How to SELECT rows in a MySQL table from a Python script
- How to INSERT rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table
- How to create a Python Virtual Environment

## Author

This project was completed as part of the Holberton School curriculum.