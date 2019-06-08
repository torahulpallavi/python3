#!/usr/bin/python

import psycopg2
import csv
import sys 

 print  sys.argv[1]
 print sys.argv[2]
 print sys.agr[3]

 

conn = psycopg2.connect('host=localhost dbname=x user=sys.agrv[2] password=sys.agrv[3]')
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











