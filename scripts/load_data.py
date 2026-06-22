#!/usr/bin/env python3
import sqlite3
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / 'data' / 'db.sqlite'
CSV = ROOT / 'dbt_project' / 'seeds' / 'jobs.csv'

def create_db():
    conn = sqlite3.connect(DATA)
    cur = conn.cursor()
    cur.execute('''
    create table if not exists jobs (
        id integer primary key,
        title text,
        company text,
        salary integer,
        posted_date text
    )
    ''')
    conn.commit()
    cur.execute('delete from jobs')
    with open(CSV, newline='') as f:
        reader = csv.DictReader(f)
        rows = [(int(r['id']), r['title'], r['company'], int(r['salary']), r['posted_date']) for r in reader]
    cur.executemany('insert into jobs(id,title,company,salary,posted_date) values (?,?,?,?,?)', rows)
    conn.commit()
    conn.close()
    print('Loaded', len(rows), 'rows into', DATA)

if __name__ == '__main__':
    create_db()
