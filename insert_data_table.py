import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Wisdom", "Adetokun Adewale 7")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")


'''
NOTE to insert mulltiple value into your table 

val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21')
]

mycursor.executemany(sql, val)

'''