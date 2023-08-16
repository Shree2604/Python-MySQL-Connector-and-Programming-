import mysql.connector

conn = mysql.connector.connect(host ="localhost", user ="root", passwd ="",database ="pythondb3")

cur = conn.cursor()

dbs = cur.execute("CREATE TABLE STUDENT(IDNO INT(4),NAME VARCHAR(50),CLASS CHAR(5))")

conn.close()
