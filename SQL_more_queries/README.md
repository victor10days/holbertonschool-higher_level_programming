# SQL - More queries

## Description
This project is part of the Holberton School curriculum **[Foundations v2.1 - Part 2]**.  
It builds upon the previous SQL project and dives deeper into the use of **MySQL** for user management, database design, and advanced data retrieval techniques.  

You will learn how to:
- Create and manage MySQL users and privileges
- Enforce constraints such as `PRIMARY KEY`, `FOREIGN KEY`, `NOT NULL`, and `UNIQUE`
- Perform complex queries across multiple tables
- Use subqueries and joins
- Work with unions and aggregations to analyze data

---

## Resources
Read or watch:
- [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
- [How To Use MySQL GRANT Statement To Grant Privileges To a User](https://www.mysqltutorial.org/mysql-grant.aspx)
- [MySQL constraints](https://www.mysqltutorial.org/mysql-constraints.aspx)
- [Basic query operation: the join](https://www.sqltutorial.org/sql-join/)
- [SQL technique: multiple joins and the DISTINCT keyword](https://www.sqlshack.com/how-to-use-sql-distinct-with-joins/)
- [SQL technique: join types](https://www.w3schools.com/sql/sql_join.asp)
- [SQL technique: subqueries](https://www.mysqltutorial.org/mysql-subquery/)
- [SQL technique: UNION and MINUS](https://www.sqltutorial.org/sql-union/)
- [MySQL Cheat Sheet](https://www.mysqltutorial.org/mysql-cheat-sheet.aspx)
- [The Seven Types of SQL Joins](https://chartio.com/learn/sql-tips/sql-join-types/)
- [MySQL Tutorial](https://www.mysqltutorial.org/)
- [SQL Style Guide](https://www.sqlstyle.guide/)
- [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)

Extra resources on relational database model design:
- [Database Design](https://www.guru99.com/database-design.html)
- [Normalization](https://www.studytonight.com/dbms/database-normalization.php)
- [ER Modeling](https://www.lucidchart.com/pages/er-diagrams)

---

## Learning Objectives
By the end of this project, you should be able to explain:
- How to create a new MySQL user
- How to manage user privileges for databases and tables
- What a `PRIMARY KEY` and `FOREIGN KEY` are and their purpose
- How to use `NOT NULL` and `UNIQUE` constraints
- How to retrieve data from multiple tables in one query
- What subqueries are and when to use them
- The difference between `JOIN` and `UNION`

---

## Requirements
- All scripts will be tested on **Ubuntu 20.04 LTS** using **MySQL 8.0.25**
- All files should end with a new line
- All SQL queries must include a descriptive comment at the top
- All SQL keywords must be in uppercase (`SELECT`, `WHERE`, etc.)
- A `README.md` file is mandatory at the root of the project folder
- The length of your files will be tested using `wc`
- Allowed editors: `vi`, `vim`, `emacs`

---

## Installation
To install MySQL 8.0 on Ubuntu 20.04:
```bash
sudo apt update
sudo apt install mysql-server
mysql --version
