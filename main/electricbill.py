import sqlite3
from cbill import bill

conn=sqlite3.connect('electric_bill.db')

c=conn.cursor()



question=input("do you want to setup the application? Respond with 'y' to setup, 'n' to skip (only for first time)@ ")
if question=='y':
  c.execute("""CREATE TABLE electricbill (
            date integer,
            pu integer,
            tamount integer
            )""")
else:
    pass


pu = 0.0
time = 0
n = int(input("enter number of appliances in your home: "))
for i in range(n):
        pr = float(input("what is the power rating of the appliance:  " + " " + str(i+1) + ":"))
        t = int(input("how many hours did u run it for: "))
        pu+=(pr*t/1000)
if pu<=100:
        amount = pu * 4.22
elif pu>100 and pu<=200:
        amount = (100 * 4.22) + (pu-100) * 5.02
else:
        amount = (100 * 4.22) + (100 * 5.02) + (pu-200) * 5.87
print("fixed charge of rupees 40 and energy duty of 0.15 rupees per unit is applicable")
tamount = amount + 40 + (pu*0.15)
print("the total bill is: " + str((tamount)))

date=input('enter date in the form dd-mm-yyyy: ')


amt=bill(date,pu,tamount)


c.execute("INSERT INTO electricbill VALUES (?,?,?)", (amt.date,amt.pu,amt.tamount))

print("data added")

conn.commit()

ch=input("Do you want to check the bill history? Press y to continue, press n to end: ")

if ch=='y':
    datefinder=input("enter date")
    c.execute("SELECT * FROM electricbill WHERE date=?", (datefinder,))
    print("Here is the data in the form (date,average power consumption(KWh), bill(in rupees):")
    print(c.fetchall())
    
input("Enter a key to continue")

conn.commit()

conn.close()

