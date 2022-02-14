
import mysql
import mysql.connector

conn=mysql.connector.connect(host='localhost',
                            user="root",
                            password="root",
                            database="ELECTRICBILL")
if conn.is_connected():
    print("Success")
cursor=conn.connect()
