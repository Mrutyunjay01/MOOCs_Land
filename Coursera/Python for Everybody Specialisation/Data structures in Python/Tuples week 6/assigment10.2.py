# -*- coding: utf-8 -*-

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counterHours = {}
for line in handle:
    if line.startswith('From '):
        if line.split()[-2].split(':')[0] not in counterHours:
            counterHours[line.split()[-2].split(':')[0]] = 1
        else: counterHours[line.split()[-2].split(':')[0]] += 1
        
for key, value in sorted(counterHours.items()):
    print(key, value)