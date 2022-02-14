
import mysql
import mysql.connector

conn=mysql.connector.connect(host='localhost',
                            user="root",
                            password="root",
                            database="ELECTRICBILL")
if conn.is_connected():
    print("""--------------------------------Electricity Billing System----------------------------------
    
    """)
    print("""--------------------------------Version 1.1-------------------------------------------------
    
    """)
cursor=conn.connect()
cur=conn.cursor()
question=input("""do you want to setup the application? Respond with 'y' to setup, 'n' to skip (only for first time): 
""")
if question=='y':
  cur.execute("""CREATE TABLE electricbill (
            date integer,
            pu integer,
            tamount integer
            );""")
  print("""Finished setting up the application
  
  """)
else:
   pass

conn.commit()
conn.close()
