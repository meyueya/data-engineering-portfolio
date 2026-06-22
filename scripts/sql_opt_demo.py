#!/usr/bin/env python3
import sqlite3
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / 'data' / 'db.sqlite'

conn = sqlite3.connect(DB)
cur = conn.cursor()
print('EXPLAIN BEFORE:')
for row in cur.execute("EXPLAIN QUERY PLAN select * from jobs where lower(title) like '%engineer%';"):
    print(row)

print('\nEXPLAIN AFTER:')
for row in cur.execute("EXPLAIN QUERY PLAN select * from jobs where salary > 90000 order by salary desc;"):
    print(row)

conn.close()
