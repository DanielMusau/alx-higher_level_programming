#!/usr/bin/python3
"""Script that takes in an argument and displays all
values in the states table."""
import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database
                         )

    cur = db.cursor()
    cur.execute(f"SELECT * FROM states \
                 WHERE CONVERT(`name` USING Latin1) \
                 COLLATE Latin1_General_CS = '{state_name}';"
                 )

    rows = cur.fetchall()

    for row in rows:
        print(row)
