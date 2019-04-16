import psycopg2
import csv
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=pa55word")
print "connection successfull"
cur = conn.cursor()
with open('name.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row.
    for row in reader:
        cur.execute(
            "INSERT INTO name VALUES (%s, %s)",
            row
        )
conn.commit()






