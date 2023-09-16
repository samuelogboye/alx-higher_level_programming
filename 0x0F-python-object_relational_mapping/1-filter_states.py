#!/usr/bin/python3
"""
A script that lists all states from the database
'hbtn_0e_0_usa'
"""

import MySQLdb

from sys import argv


if __name__ == '__main__':
    """
    connect to the database and execute the querry that
    will fetch all data from the 'states' table
    """
    db = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    rows = cur.fetchall()

    for row in rows:
        print(row)
