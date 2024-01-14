#!/usr/bin/python3
"""Script that list all states with a name starting with N from database"""
import sys
import MySQLdb


if __name__ == "__main__":
    """Main execution"""
    db = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            host="localhost",
            port=3306
            )

    cursor = db.cursor()

    cursor.execute(
            "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
            )

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()