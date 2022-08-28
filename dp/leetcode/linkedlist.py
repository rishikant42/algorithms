class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)

        if (self.head):
            current = self.head

            while(current.next):
                current = current.next
            current.next = node
        else:
            self.head = node

    def printLL(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next



ll = LinkedList()

ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.printLL()
