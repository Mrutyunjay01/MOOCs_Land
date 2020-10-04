# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 21:38:53 2020

@author: MRUTYUNJAY BISWAL
"""

import sqlite3

connector = sqlite3.connect('rosterdb.sqlite')
cursor = connector.cursor()

cursor.execute('''
SELECT hex(User.name || Course.title || Member.role ) AS X 
FROM User JOIN Member JOIN Course 
ON User.id = Member.user_id AND Member.course_id = Course.id
ORDER BY X
''')

print(cursor.fetchone())