#!/usr/bin/python3
""" States Module
    Contains States MySql query functions
"""

import sys
import MySQLdb


def all_states():
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
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()
    cursor.close()
    database.close()
    for row in states:
        print(row)


if __name__ == '__main__':
    all_states()
