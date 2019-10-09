#!/usr/bin/python3
"""
query all 'cities' of a provided state parameter using MySQLdb
args: [mysql username] [mysql password] [database name] [state name]
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()
    cur.execute(
        "SELECT cities.name FROM cities \
        JOIN states ON cities.state_id = states.id WHERE states.name = %s \
        ORDER BY cities.id ASC", [sys.argv[4]])

    rows = cur.fetchall()
    print(', '.join(row[0] for row in rows))

    cur.close()
    db.close()
