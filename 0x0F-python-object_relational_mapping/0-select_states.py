#!/usr/binpython3
"""
Lists all states in the database
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
            sb=sys.argv[3], port=3306)

    curl = db.cursor()
    cur.execute("SELECT * FROM states;")
    states = cur.fetchall()

    for states in states:
        print(states)
