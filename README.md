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

Using Gitpod:

https://github.com/Code-Institute-Org/gitpod-database-config

Click on Use This Template to create a repo based on this setup.

Then click on GITPOD, not forgetting to click on Expose when that option is available.

Use pip3 install pymysql to install pymysql library

Grab data from github.

wget https://raw.githubusercontent.com/lerocha/chinook-database/master/ChinookDatabase/DataSources/Chinook_MySql_AutoIncrementPKs.sql

Chinook_MySql_AutoIncrementPKs.sql -v

pip3 freeze > requirements.txt

echo '*.sql' >> .gitignore


- Created cursor and then use the cursor to execute queries.
- Use for to print rows
- Depending on type of cursor used, result can be a Tuple or a Dictionary etc.
