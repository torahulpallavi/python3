import psycopg2
import csv
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres")
print "connection successfull"
cur = conn.cursor()

with open('scripts/name.csv', 'r') as f:
    cur.copy_from(f, 'name', sep=',') # name of the table and seprator
    conn.commit()

    print "[INFO] data loaded successfully" 


'''

with open('name.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row.
    for row in reader:
        cur.execute(
            "INSERT INTO name VALUES (%s, %s)",
            row
        )
'''











