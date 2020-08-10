#!/usr/bin/python3
""" States Module
    Contains States MySql query functions
"""

import sys
import MySQLdb


def n_states():
    """ Print filtered by N States from database
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
                    WHERE name REGEXP '(?-i)^[N]'\
                    ORDER BY id ASC")
    states = cursor.fetchall()
    for row in states:
        print(row)
    cursor.close()
    database.close()


if __name__ == '__main__':
    n_states()
