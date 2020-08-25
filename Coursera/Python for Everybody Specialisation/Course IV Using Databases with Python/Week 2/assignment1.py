# -*- coding: utf-8 -*-

import sqlite3

connector = sqlite3.connect('Assignment1.sqlite')
cursor = connector.cursor()

cursor.execute('DROP TABLE IF EXISTS Ages')

cursor.execute('''CREATE TABLE Ages(name VARCHAR(128), age INTEGER)''')

cursor.execute('DELETE FROM Ages')

for _ in range(6):
    name, age = input().split()
    print(name, age)
    cursor.execute('''
                   INSERT INTO Ages (name, age) VALUES (?, ?)
                   ''', (name, age, ))
                   
                   
for row in cursor.execute('SELECT * FROM Ages'):
    print(row)
    
for row in cursor.execute('SELECT hex(name || age) AS X FROM Ages ORDER BY X'):
    print(row)

cursor.close()
