#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    """
    connect to the database and execute the querry that
    will fetch all name of a state as an argument and lists all cities
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

    cur.execute("SELECT cities.name \
        FROM cities JOIN states ON cities.state_id = states.id \
        WHERE states.name LIKE BINARY %(name)s \
        ORDER BY cities.id ASC", {'name': argv[4]})

    rows = cur.fetchall()

    # Extract city names and concatenate them
    city_names = [row[0] for row in rows]
    city_list = ", ".join(city_names)

    print(city_list)

    # Close the cursor and the database connection
    cur.close()
    db.close()
