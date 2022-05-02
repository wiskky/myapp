#You must firstly install mysql-connector-python using pip install command.
import mysql.connector

#password to the database
mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = ""
	)

mycursor = mydb.cursor()

#creating database 
mycursor.execute("CREATE DATABASE pythonworld")

#checking if the database has been created
mycursor.execute("SHOW DATABASES")
for x in mycursor:
 	print("Database created")
