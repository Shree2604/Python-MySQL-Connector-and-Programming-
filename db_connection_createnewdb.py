import mysql.connector

conn = mysql.connector.connect(host ="localhost", user ="root", passwd ="")

cur = conn.cursor()

dbs = cur.execute("create database PythonDB3")

conn.close()
