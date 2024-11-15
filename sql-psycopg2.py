import psycopg2

connection = psycopg2.connect("dbname=chinook user=postgres password=Mohanad")

cursor = connection.cursor()

cursor.execute('SELECT * from "Artist" where "Name"=%s',["test"])

results = cursor.fetchall()

cursor.close()

for result in results:
    print(result)