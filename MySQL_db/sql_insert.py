import mysql.connector
def insert_data(id,name,country):
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="roottoor",
    database="bhavana_ece"
  )
  mycursor = mydb.cursor()

  sql = "INSERT INTO city (id,name,country) VALUES(%s, %s,%s)"
  val = [id,name,country]
  mycursor.execute(sql, val)

  mydb.commit()
  print("Record Inserted")

id = input("Enter id: ")
name = input("Enter name: ")
country = input("Enter country: ")
insert_data(id,name,country)