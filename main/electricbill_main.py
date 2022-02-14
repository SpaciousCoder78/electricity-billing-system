
import mysql
import mysql.connector

con=mysql.connector.connect(host='localhost',
                            user="root",
                            password="root",
                            database="ELECTRICBILL")
if con.is_connected():
    print("Success")