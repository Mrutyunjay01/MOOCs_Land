# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 02:18:53 2020

@author: MRUTYUNJAY BISWAL
"""


class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode = None


def circular_check(node):
    marker1 = marker2 = node

    while marker1 is not None and marker2.nextnode is not None:

        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode  # move it faster than marker1

        if marker2 == marker1:
            return 2

    return False
    pass
