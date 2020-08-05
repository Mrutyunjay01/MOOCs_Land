# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 22:02:21 2020

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
        

class FootballFan(partyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, 'Points', self.points)
        

if __name__=='__main__':
    j = FootballFan('Jim')
    j.party()
    j.touchdown()