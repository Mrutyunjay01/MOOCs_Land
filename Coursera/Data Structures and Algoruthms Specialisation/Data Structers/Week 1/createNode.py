# -*- coding: utf-8 -*-


class Node:
    """ Create a Node Class"""
    def __init__(self, value):
        
        self.key = value
        self.nextnode = None
        
class DoublyLinkedList:
    
    def __init__(self, value):
        
        self.value = value
        self.nextnode = None
        self.prevnode = None
        
    