# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 16:21:30 2020

@author: MRUTYUNJAY BISWAL
"""
class partyAnimal:
    
    x = 0
    name = ""
    
    def __init__(self, nam):
        self.name = nam
        print(self.name, 'Constructed')
        
    def party(self):
        self.x = self.x + 1
        print(self.name, 'Party count', self.x)
        
if __name__=='__main__':
    
     s = partyAnimal('Sally')
     s.party()
     