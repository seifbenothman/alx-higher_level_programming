#!/usr/bin/python3
"""
    A script that lists all cities from the database hbtn_0e-0-usa
    Username, password and database names are given as user args
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """Main execution"""
    db = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            host="localhost",
            port=3306)

    cursor = db.cursor()

    query = """SELECT c.id, c.name, s.name
            FROM states s, cities c
            WHERE c.state_id = s.id
            ORDER BY id ASC"""

    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
