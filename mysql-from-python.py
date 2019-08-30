import os
import datetime
import pymysql

# Get username
username = os.getenv('gitpod')

connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    #Run a query
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        rows = [("Bob", 21, "1990-02-06 23:04:56"),
                ("Luke", 12, "2501-03-05 02:30:11"),
                ("Leia", 12, "2501-03-05 02:30:15"),
                ("Sand Person", 24, "2498-04-08 05:45:21")]
        cursor.executemany("INSERT INTO Friends VALUES (%s, %s, %s);", rows)
        connection.commit()

finally:
    #Close the connection, regardless of whether the above was successful
    connection.close