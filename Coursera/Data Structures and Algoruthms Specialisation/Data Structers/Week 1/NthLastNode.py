# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 02:42:48 2020

@author: MRUTYUNJAY BISWAL
"""

class Node:
    """ Create a Node Class"""
    def __init__(self, value):
        
        self.key = value
        self.nextnode = None

def nth_last_node(n, head):
    
    left_pointer = head
    right_pointer = head
    
    for _ in range(n-1):
        
        if not right_pointer.nextnode:
            raise LookupError('N is larger than the linkedlist')
            
        right_pointer = right_pointer.nextnode
        
    while right_pointer.nextnode: # it hasn't reached Null pointer
        
        left_pointer = left_pointer.nextnode
        right_pointer = right_pointer.nextnode
        
    return left_pointer
     