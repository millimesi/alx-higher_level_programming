#!/usr/bin/python3
'''
select and show the table content
'''


import sys
import MySQLdb

if __name__ == "__main__":
    host = 'localhost'
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    port = 3306
    connection = MySQLdb.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=port
    )
    cur = connection.cursor()
    sql_query = ("SELECT cities.id, cities.name, states.name FROM cities "
                 "JOIN states ON cities.state_id = states.id")
    cur.execute(sql_query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    connection.close()
