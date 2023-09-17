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
    # Check if the correct number of arguments are provided
    if len(argv) != 5:
        print("Usage: ./script.py <username> <password>\
            <database> <name_to_search>")
        exit(1)

    db = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    cur = db.cursor()

    # Create the SQL query with string formatting
    #  to prevent SQL injection
    cur.execute(
        "SELECT * FROM states WHERE name LIKE\
                    BINARY %(name)s ORDER BY states.id ASC", {'name': argv[4]})

    rows = cur.fetchall()

    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cur.close()
    db.close()
