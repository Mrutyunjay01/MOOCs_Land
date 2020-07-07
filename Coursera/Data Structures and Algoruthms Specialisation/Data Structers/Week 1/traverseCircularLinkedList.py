class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
    # add code here


class CircularLinkedList:

    def __init__(self):
        # crate an empty circular Linked List
        self.head = Node(None)
        self.tail = Node(None)

    def push(self, data):
        node = Node(data)
        node.value = data

        if self.head.value is None:
            self.head = node
            self.head.next = self.head

        else:
            node.next = self.head
            if self.tail.value is None:
                self.tail = self.head
            self.tail.next = node
            node, self.head = self.head, node

    #  Function to print nodes in a given Circular linked list
    def printList(self):
        ans = []
        current_head = self.head
        ans.append(current_head.value)

        while current_head.next != self.head:
            current_head = current_head.next
            ans.append(current_head.value)

        print(" ".join([str(a) for a in ans]))


if __name__ == '__main__':
    for _ in range(int(input())):

        cl = CircularLinkedList()
        l = list(map(int, input().strip().split()))

        for i in range(0, len(l)):
            cl.push(l[i])

        cl.printList()
        pass
