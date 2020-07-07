# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 02:31:38 2020

@author: MRUTYUNJAY BISWAL
"""
class Node:
    """ Create a Node Class"""
    def __init__(self, value):
        
        self.key = value
        self.nextnode = None


def reverse(head):
    
    current = head
    previous = None
    nextnode = None
    
    while current:
        nextnode = current.nextnode
        current.nextnode = previous
        previous = current
        current = nextnode
        
    return previous

