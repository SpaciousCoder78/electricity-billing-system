# electricity-billing-system
A simple and efficient electricity billing system designed using MySQL and Python

# Pre-requisites:

You need to have the following pre-requisites on your PC in order to run the application. Prerequisites are included in the installation folder,

- Python 3.9
- MySQL 8.0.28


# User's Manual:

This user manual will guide you through the steps necessary to use the software. 
Before you use the software, make sure that you have the following software which are necessary for the software to run.
Required Software:
-	Python 3.9
-	MySQL 8.0.28


# Setup:
Before you start calculating electricity bills, you are required to use the built in setup to configure the database. 
Note: If you use MySQL and happen to have an existing table called ‘electricbill’, please use MySQL Command Line Client and type DROP TABLE electricbill. The software needs to create a electricbill table via the setup process and an  existing database named electricbill will interrupt the setup process.
 
To use the setup, just open the file electricbill_main.py file and you’ll be greeted with a menu.
 

Now you’re required to type the number ‘5’ and hit enter.
Doing this will start the first time setup and the setup will create a new table called electricbill. This is the table where the bills will be stored.
 
# Calculating an Electricity Bill
Before you calculate an electricity bill, you’re required to have the following data:
-	Types of appliances at your home
-	Power consumption of each appliance (in KWh)
-	Usage period of each appliance (in hours)
Once you have the following data, you can launch the main python file again
You’ll be greeted by the menu once again
 

This time you have to press ‘1’ and hit enter
Once you do that, the software will now ask for your name
 
Enter your name and hit enter
Note: Names are case sensitive 
Then the program will ask you for the number of appliances at your home, kindly enter the number and hit enter.
The program then asks for wattage and usage time for each appliance. Enter the details and hit enter.
The program will now utilize the built in algorithm and calculate the electricity bill
 
We are now required to store the bill in the database so the user has to enter the month in which the bill was calculated, this will store the bill in the database.
 
Note: The date must be in the form mm-yyyy. Using any other format will cause errors and the bill will not be entered into the database.
If you don’t get any errors after entering the date, it means that the bill is entered into the database.

# View bills that are stored in the database
If you wish to check the bills that are stored in the database, you can use the number ‘2’ for checking one bill at a time or number ‘3’ for checking all bills from the database
If you press ‘2’ , you’ll be greeted with a ‘Enter the month’ option.
Type the month of the bill, followed by your name (Case Sensitive)
 
The program will now display the bill from the specified date
 

If you press ‘3’ in the menu, you’ll be greeted with “Enter your name” option
Enter your name to check all the bills created by the mentioned user.

 

# View Wattage of Common Appliances at your home

If you wish to know the wattages of common appliances at your home, use ‘4’ in the menu to view them

 

# View Software Information

If you wish to know the software version of MySQL , Python and view the patch notes, press ‘6’ in the menu
 


