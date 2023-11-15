import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="db_demos",
    user="postgres",
    password="1123QwER")
cur = conn.cursor()
cur.execute("SELECT * FROM cities")
# conn.commit()
for row in cur.fetchall():
    print(row)

conn.close()