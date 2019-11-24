class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

    def __str__(self):
        return self.value

class DoublyLinkedList:

    def __init__(self):
            self.head = None

    def clear(self):
        self.__init__()
               
    def insertAtStart(self, val):

        if self.head is None:
            new_node = Node(val)
            self.head = new_node
            return

        new_node = Node(val)
        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node

    def insert_at_end(self, val):

        if self.head is None:
            new_node = Node(val)
            self.head = new_node
            return

        n = self.head
        while n.next is not None:
            n = n.next
        new_node = Node(val)
        n.next = new_node
        new_node.previous = n

    def reverser(self):

        if self.head is None :
            return
        
        f = self.head
        n = f.next
        f.next = None
        f.previous = n
        while n is not None : 
            n.previous = n.next
            n.next = f
            f = n
            n = n.previous
        self.head = f

    def traverse_list(self):
        if self.head is None:
            return("List has no elements")
            
        else:
            strr=''
            n = self.head
            while n is not None:
                strr += n.value + " "
                n = n.next
            return strr