# python3

#import sys
#import threading

class Node:
    
    def __init__(self, key):
        self.key = key
        self.children = []
        
    def addChild(self, Child):
        self.children.append(Child)
    
    def children(self):
        return self.children
        

class Tree:
    
    def __init__(self):
        self.nodes = {}
        self.root = None
        
    def make_tree(self, nodes):
        
        for child_index in range(len(nodes)):
            parent_index = nodes[child_index]
            #print(parent_index)
            if parent_index == -1:
                self.root = Node(child_index)
                self.nodes[self.root.key] = self.root
            else:
                if parent_index not in self.nodes.keys():
                    self.nodes[parent_index] = Node(parent_index)
                if child_index in self.nodes.keys():
                    self.nodes[parent_index].addChild(self.nodes[child_index])  
                else:
                    self.nodes[parent_index].addChild(child_index)
                
    def __repr__(self):
        return 'Root of the tree is: {}'.format(self.root.key)


def compute_height(n, parents):
    # Replace this code with a faster implementation
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height

def effcmhgh(tr):
    
    if not len(tr.root.children):
        return 1
    
    children = tr.root.children
    
    
    pass

def main():
    for _ in range(int(input())):
        nodes = list(map(int, input().strip().split()))
        tree = Tree()
        tree.make_tree(nodes)
        print(tree.root.key)
        for child in tree.root.children:
            if isinstance(child, Node):
                print(child.children)
#        for node in tree.nodes.keys():
#            print(node, tree.nodes[node].children)

if __name__ == '__main__':
    main()
# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
#sys.setrecursionlimit(10**7)  # max depth of recursion
#threading.stack_size(2**27)   # new thread will get stack of such size
#threading.Thread(target=main).start()
