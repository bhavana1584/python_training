import mysql.connector
def display_data():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="roottoor",
    database="bhavana_ece"
  )
  mycursor = mydb.cursor()
  mycursor.execute("select * from city")

  result = mycursor.fetchall()
  for row in result:
    print(row)

  print("Done")

display_data()