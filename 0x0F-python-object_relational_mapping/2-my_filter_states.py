#!/usr/bin/python3
"""
A script that takes in an argument and display all values in the states table
from the database 'hbtn_0e_0_usa' where name matches the argument
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    """
    connect to the database and execute the querry that
    will fetch all data from the 'states' table where name matches the argument
    """
    db = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (argv[4],))

    rows = cur.fetchall()

    for row in rows:
        print(row)
