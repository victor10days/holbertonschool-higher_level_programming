#!/usr/bin/python3
'''Takes name of a state as an argument and lists all cities of that state.'''

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])
    cursor = db.cursor()
    query = """SELECT cities.name FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC"""
    cursor.execute(query, (sys.argv[4],))
    results = cursor.fetchall()
    city_names = [row[0] for row in results]
    print(", ".join(city_names))
    cursor.close()
    db.close()
