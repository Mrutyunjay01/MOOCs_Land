# -*- coding: utf-8 -*-
def general():
    hand = open('SRIP list.txt')
    for line in hand:
        #print(len(line))
        line = line.rstrip()
        
        if line.find('Done') >= 0:
            print(line)
    pass

def regex():
    import re
    
    hand = open('SRIP list.txt')
    for line in hand:
        line = line.rstrip()
        if re.search('Done', line):
            print(line)
    pass
# using re.search alike startswith method of string
def alikeStartswith():
    import re
    hand = open('SRIP list.txt')
    for line in hand:
        line = line.rstrip()
        if re.search('^[a-z0-9]', line):
            print(line)
            
    pass

if __name__ == '__main__':
    #general()
    #regex()
    alikeStartswith()
