#!/usr/bin/python3
""" States Module
    Contains Cities MySql query functions
"""

import sys
import MySQLdb


def all_cities():
    """ Print all States from database
    """

    database = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host='localhost',
        port=3306
    )
    cursor = database.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name\
                    FROM cities, states\
                    WHERE cities.state_id = states.id\
                    ORDER BY cities.id ASC")
    states = cursor.fetchall()
    for row in states:
        print(row)
    cursor.close()
    database.close()


if __name__ == '__main__':
    all_cities()
