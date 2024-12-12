class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CLL:
    def __init__(self):
        self.head = None
    
    def insert_at_front(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            new.next = new
        else:
            curr = self.head
            while curr:
                curr = curr.next
                if curr.next == self.head:
                    break
            curr.next = new
            new.next = self.head
            self.head = new
    
    def insert_at_end(self, data):
        new = Node(data)
        if self.head == None:
            self.head = new
            new.next = new
        else:
            curr = self.head
            while curr:
                curr = curr.next
                if curr.next == self.head:
                    break
            curr.next = new
            new.next = self.head
    
    def display(self, head):
        curr = head
        while curr:
            print(curr.data, end = " -> ")
            curr = curr.next
            if curr == head:
                break
        print(curr.data)

list1 = CLL()
list1.insert_at_end(44)
list1.insert_at_front(11)
list1.insert_at_front(22)
list1.insert_at_front(33)
list1.insert_at_end(55)
list1.insert_at_front(66)

list1.display(list1.head)