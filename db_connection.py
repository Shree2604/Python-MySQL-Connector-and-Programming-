import mysql.connector

conn = mysql.connector.connect(host="localhost",user ="root",passwd ="")

print(conn)
