# -*- coding: utf-8 -*-

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    for word in line.rstrip().split():
        if word not in lst:
            lst.append(word)
    
print(sorted(lst))