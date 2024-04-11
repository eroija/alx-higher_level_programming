#!/usr/bin/python3
# lists all states from the database hbtn_0e_0_usa


import MySQLdb

# Connect to MySQL server
db = MySQLdb.connect(host="localhost",
                     user="{username}",
                     password="{password}",
                     database="{database_name}")

cursor = db.cursor()
sql = "SELECT * FROM states ORDER BY states.id ASC;"
cursor.execute(sql)

states = cursor.fetchall()
for state in states:
    print(state[0], state[1])

cursor.close()
db.close()

if __name__ == "__main__":
