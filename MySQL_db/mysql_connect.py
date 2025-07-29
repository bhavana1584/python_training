import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="roottoor",
  database="bhavana_ece"
)

print("Database Connected")
