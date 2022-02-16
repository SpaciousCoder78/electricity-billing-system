from classes import bill
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
   question=input("""do you want to setup the application? Respond with 'y' to setup, 'n' to skip (only for first time): 
   """)
   
   
   print("""Finished setting up the application
        """)
   cur.execute("""CREATE TABLE electricbill (
            name varchar(30), 
            date integer,
            pu integer,
            tamount integer
            );""")
   
   




def calc(x):
   pu=0.0
   time=0
   date=0000-00-00
   n=int(input("Enter no of appliances:"))
   name = input("enter your name")
   for i in range(n):
      pr=float(input("Power rating of the appliance: "+" "+ str(i+1)+ ":"))
      t=int(input("""Enter the usage time(in hours)

         """))
      pu+=(pr*t/1000)
   if pu<=100:
      amount= pu * 4.22
   elif pu>100 and pu<=200:
      amount=(1004.22)+(pu-100)*5.02
   else:
      amount = (100 * 4.22) + (100 * 5.02) + (pu-200) * 5.87
   print("""Fixed charge of rupees 40 and energy duty of 0.15 rupees per unit is applicable

      """)
   tamount = amount + 40 + (pu*0.15)
   date=input("""Enter the date of the bill in the form dd-mm-yyyy: 

      """)
   
   sql="INSERT INTO electricbill(name,date,pu,tamount) VALUES('{}','{}','{}','{}');".format(name,date,pu,tamount)
   cur.execute(sql)
   cur.execute("ALLOW INVALID DATES")
   conn.commit()

def comm_appliance(y):
     
        print("----------------------------Wattage of Common Appliances---------------------------")
        print ("""No. Appliance                      Min    Max    Standby
         1.  32 InchLEDTV                    20W    60W    1W
         2.  Refrigerator                    100W   200W   N/A
         3.  Washing Machine                 500W   500W   1W
         4.  100W light bulb (Incandescent)  100W   100W   0W
         5.  Electric Pressure Cooker        1000W  1000W  N/A
         6.  Inverter Air conditioner        1300W  1800W  N/A
         7.  Iron                            1000W  1000W  N/A
         8.  Laptop Computer                 50W    100W   N/A
         9.  LED Light Bulb                  7W     10W    0W
         10.  Pedestal Fan                   50W    60W    N/A""")
    

def softinfo(z):
      print("-----------------------------Software Information----------------------")
      print("Version: 1.1")
      print("Last Patch: 15/2/2022")
      print("Python version: 3.9")




def menu(a):
   if menyoo==1:
      calc(menyoo)
   elif menyoo==2:
      print(2)
   elif menyoo==3:
      comm_appliance(menyoo)
   elif menyoo==4:
      setup(menyoo)
   elif menyoo==5:
      print(48)
   elif menyoo==6:
      softinfo(menyoo)
   
print("------------------------------Main Menu-----------------------------")
print("1.Calculate a electricity bill")
print("2.View previous bills")
print("3.View wattage of common appliances")
print("4.Installation Setup for firsttimers")
print("5.Exit the application")
print("6.Software Information")
print()
menyoo=(int(input("Enter your choice(1-5):  ")))
menu(menyoo)


conn.commit()
conn.close()
