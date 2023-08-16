# Section 1 starting point
import mysql.connector

conn = mysql.connector.connect(host ="localhost", user ="root", passwd ="")

cur = conn.cursor()

# Section 1 ending point

# Database coding starting from here

dbs = cur.execute("show databases")


# Database coding ending from here


# Database output coding starting from here

for i in cur:
    print(i)

# Database output coding ending from here

conn.close()
