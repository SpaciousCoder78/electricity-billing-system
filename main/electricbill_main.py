
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
def setup(q):
   if question=='y':
     print("""Finished setting up the application
        """)
     cur.execute("""CREATE TABLE electric (
            date integer,
            pu integer,
            tamount integer
            );""")
   else:
    pass
      

question=input("""do you want to setup the application? Respond with 'y' to setup, 'n' to skip (only for first time): 
   """)
setup(question)

conn.commit()
conn.close()
