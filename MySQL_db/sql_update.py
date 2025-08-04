import mysql.connector

def update_data(name,id,country):
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="roottoor",
    database="bhavana_ece"
  )
  mycursor = mydb.cursor()
  # sql = "UPDATE city SET name = 'Frankfurt' WHERE id = 2"
  # mycursor.execute(sql)
  sql = "UPDATE city SET name = %s,country = %s WHERE id = %s"
  val = [name,country,id]
  mycursor.execute(sql,val)

  mydb.commit()
  print("Data Updated")

name = input("Enter new name: ")
country = input("Enter new country: ")
id = input("Enter id to change: ")
update_data(name,id,country)