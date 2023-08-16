import mysql.connector

conn = mysql.connector.connect(host ="localhost", user ="root", passwd ="",database ="pythondb3")

cur = conn.cursor()

dbs = cur.execute("ALTER TABLE STUDENT ADD PRIMARY KEY(IDNO)")

conn.close()
