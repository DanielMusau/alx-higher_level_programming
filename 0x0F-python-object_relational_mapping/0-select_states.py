#!/usr/bin/python3
"""Script tht lists all states from database."""
import MySQLdb


db = MySQLdb.connect(host="localhost",
                     port=3306,
                     user="root",
                     passwd="D@nnyb0y",
                     db="hbtn_0e_0_usa"
                     )
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC;")
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
db.close()
