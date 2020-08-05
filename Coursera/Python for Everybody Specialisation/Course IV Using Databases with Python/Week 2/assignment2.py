# -*- coding: utf-8 -*-

import sqlite3

# set up the connector
conn = sqlite3.connect('emaildb_assignment.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
            CREATE TABLE Counts (org TEXT, count INTEGER)
            ''')
            
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'
    
print(fname)
fh = open(fname)

for line in fh:
    if not line.startswith('From: '): continue
    
    email = line.split()[1]
    org_name = email[email.find('@')+1 : ]
    
    cur.execute('SELECT count FROM  Counts WHERE org = ?', (org_name, ))
    row = cur.fetchone()
    
    if row is None:
        cur.execute('''
                    INSERT INTO Counts (org, count) VALUES (?, 1)
                    ''', (org_name, ))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org_name, ))
        
   
conn.commit()
    
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
    
cur.close()