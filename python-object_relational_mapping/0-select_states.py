#!/usr/bin/python3
"""List tjing for state id"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db_name = argv[3]

    try:
        # Establish the database connection
        db = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=passwd, db=db_name)

        # Create a cursor object
        cursor = db.cursor()

        # Execute the SQL query to select all states sorted by id
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all rows from the executed query
        rows = cursor.fetchall()

        # Display the results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
    finally:
        # Close the cursor and the connection
        cursor.close()
        db.close()
