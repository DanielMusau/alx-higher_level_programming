#!/usr/bin/python3
"""Script that list all states with a name starting with N
from the database."""
import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database
                         )

    cur = db.cursor()
    cur.execute("SELECT * \
                 FROM states \
                 WHERE CONVERT(`name` USING Latin1) \
                 COLLATE Latin1_General_CS \
                 LIKE 'N%';")

    rows = cur.fetchall()

    for row in rows:
        print(row)
