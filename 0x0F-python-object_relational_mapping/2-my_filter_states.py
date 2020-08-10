#!/usr/bin/python3
""" States Module
    Contains States MySql query functions
"""

import sys
import MySQLdb


def find_states():
    """ Filter states with a given state name
        Sys Args:
            1: user
            2: password
            3: database
            4: state name
    """

    database = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host='localhost',
        port=3306
    )
    cursor = database.cursor()
    cursor.execute("SELECT *\
                    FROM states\
                    WHERE name LIKE '{}'\
                    ORDER BY id ASC"
                   .format(sys.argv[4]))
    states = cursor.fetchall()
    for row in states:
        print(row)
    cursor.close()
    database.close()


if __name__ == '__main__':
    find_states()
