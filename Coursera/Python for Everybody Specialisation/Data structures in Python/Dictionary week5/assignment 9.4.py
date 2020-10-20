# -*- coding: utf-8 -*-

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counter = {}
for line in handle:
    if line.startswith('From '):
        if line.split()[1] not in counter:
            counter[line.split()[1]] = 1
        else: counter[line.split()[1]] += 1
        
for key, value in counter.items():
    if value==max(counter.values()):
        print(key, value) 