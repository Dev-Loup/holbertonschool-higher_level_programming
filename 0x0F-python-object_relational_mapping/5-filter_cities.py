#!/usr/bin/python3
""" cities Module
    Contains Cities MySql query functions
"""


def cities_by_st():
    """ Print all cities in the State
    """

    database = MySQLdb.connect(user=sys.argv[1],
                               passwd=sys.argv[2],
                               db=sys.argv[3])
    cursor = database.cursor()
    cr.execute("SELECT cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s\
                ORDER BY cities.id", (sys.argv[4], ))
    state_list = cursor.fetchall()
    first = 0
    for city in state_list:
        if first != 0:
            print(", ", end="")
        print("%s" % city, end="")
        first += 1
    print("")
    cr.close()
    db.close()


if __name__ = "__main__":
    cities_by_st()
