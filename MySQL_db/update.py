import mysql.connector

def update_data():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="roottoor",
    database="bhavana_ece"
  )
  mycursor = mydb.cursor()
  sql = "UPDATE city SET name = 'Frankfurt' WHERE id = 2"
  mycursor.execute(sql)

  mydb.commit()
  print("Data Updated")

update_data()