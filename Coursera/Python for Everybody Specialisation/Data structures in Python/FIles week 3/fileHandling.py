# -*- coding: utf-8 -*-
fname = input('Enter the filename: ')
fh = open(fname)
for line in fh.readlines():
    print(line.strip().upper())
