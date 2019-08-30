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
        cursor.execute("UPDATE Friends SET age = %s WHERE name = %s;",
                    (23, 'Bob'))
        connection.commit()

finally:
    #Close the connection, regardless of whether the above was successful
    connection.close