import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    numberOfRows = cur.execute("SELECT * FROM states ORDER BY states.id")
    for a in range(numberOfRows):
        print(cur.fetchone())