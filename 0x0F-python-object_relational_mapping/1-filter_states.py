#!/usr/bin/python3
"""
filter states starting with capital 'N' using the MySQLdb module
arguments: [mysql username] [mysql password] [databasename]
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
    cur.execute("SELECT * FROM states WHERE name REGEXP BINARY '[N]'")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
