#!/usr/bin/python3
"""
display all values in a 'states' table matching user parameter
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
    cur.execute("SELECT * FROM states WHERE BINARY name = '{}' \
    ORDER BY id ASC".format(sys.argv[4]))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
