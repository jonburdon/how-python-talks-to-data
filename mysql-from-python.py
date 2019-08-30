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
        rows = [(44, 'Bob'),
                 (13, 'Luke'),
                  (13, 'Leia')]
        cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;", rows)
        connection.commit()

finally:
    #Close the connection, regardless of whether the above was successful
    connection.close