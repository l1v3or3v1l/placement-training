class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DCLL:
    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        new = Node(data)
        if self.head == None:
            self.head = new
            new.next = new
            new.prev = new
        else:
            last_node = self.head.prev
            last_node.next = new
            new.prev = last_node
            new.next = self.head
            self.head.prev = new
            self.head = new
    
    def insert_at_end(self, data):
        new = Node(data)
        if self.head == None:
            self.head = new
            new.next = new
            new.prev = new
        else:
            last_node = self.head.prev
            last_node.next = new
            new.prev = last_node
            self.head.prev = new
            new.next = self.head

    def display(self, head):
        curr = head
        while curr:
            print(curr.data, end = " <=> ")
            curr = curr.next
            if curr == self.head:
                break
        print(curr.data)
                

list1 = DCLL()
list1.insert_at_end(44)
list1.insert_at_front(11)
list1.insert_at_front(22)
list1.insert_at_front(33)
list1.insert_at_end(55)
list1.insert_at_front(66)

list1.display(list1.head)