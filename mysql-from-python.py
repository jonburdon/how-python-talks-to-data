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
        cursor.execute(""" CREATE TABLE IF NOT EXISTS
                       Friends(name char(20), age int, DOB datetime); """)
        # Note that the above will still display a Warning

finally:
    #Close the connection, regardless of whether the above was successful
    connection.close