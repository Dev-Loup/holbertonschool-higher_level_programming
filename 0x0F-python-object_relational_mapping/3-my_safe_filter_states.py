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
    the_query = "SELECT *\
                 FROM states\
                 WHERE BINARY name LIKE %s\
                 ORDER BY id ASC"
    cursor.execute(the_query, (sys.argv[4], ))
    states = cursor.fetchall()
    for row in states:
        print(row)
    cursor.close()
    database.close()


if __name__ == '__main__':
    find_states()
