import psycopg2 as pg2
import config

db = config.database
user = config.user
passw = config.password

con = pg2.connect(database=db, user=user, password=passw)

cur = con.cursor()

cur.execute('SELECT * FROM payment')

data = cur.fetchmany(10)

print(data[0])

con.close()