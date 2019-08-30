# How Python talks to data

## Learning project following Code Institute Tutorials

### This file documents the learning covered, with examples and reminder resources.

## Technologies
* Python
* MySql
* Gitpod

## Developer Aims
* Learn how to manipulate MySql data using Python:
* Cursors

## Learning Process Documentation:

### Setting up Gitpod:

https://github.com/Code-Institute-Org/gitpod-database-config

Click on Use This Template to create a repo based on this setup.

Then click on GITPOD, not forgetting to click on Expose when that option is available.

Use pip3 install pymysql to install pymysql library

Grab data from github.

    wget https://raw.githubusercontent.com/lerocha/chinook-database/master/ChinookDatabase/DataSources/Chinook_MySql_AutoIncrementPKs.sql

    Chinook_MySql_AutoIncrementPKs.sql -v

    pip3 freeze > requirements.txt

    echo '*.sql' >> .gitignore

### Using a cursor

- Created cursor and then use the cursor to execute queries.
- Use for to print rows
- Depending on type of cursor used, result can be a Tuple or a Dictionary etc.
- pymysql.cursors.DictCursor cursor type will return data as a Dictionary



### Creating a blank table

import datetime in mysql-from-python.py

        cursor.execute(""" CREATE TABLE IF NOT EXISTS
                       Friends(name char(20), age int, DOB datetime); """)

(Go to terminal, mysql to verify new table exists)

## Inserting data into a table


Create tuple for readability. See line 16: row = ("Bob", 21, "1990-02-06 23:04:56")

    cursor.execute("INSERT INTO Friends VALUES (%s, %s, %s);", row)
    connection.commit()

Run new py file from terminal.
Use mysql command line to verify Bob row has been added.

## Execute many - used to execute multiple mysql statements.

- Example would be to insert many rows at once.

Changed rows variable to be a list of tuples with row data to be added.

Change syntax to:

    cursor.executemany("INSERT INTO Friends VALUES (%s, %s, %s);", rows)

Run py file and verify in mysql command line that data is added.

## Update rows

    cursor.execute("UPDATE Friends SET age = 22 WHERE name = 'Bob';")

Run py file and verify in mysql command line that data is added.





