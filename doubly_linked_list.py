class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        new = Node(data)
        if self.head != None:
            self.head.prev = new
            new.next = self.head
        self.head = new
    
    def insert_at_end(self, data):
        new = Node(data)
        if self.head == None:
            self.head = new
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = new
            new.prev = curr

    def delete(self, data):
        if self.head.data == data and self.head.next:
            self.head = self.head.next
            self.head.prev = None
        curr = self.head
        while curr.next.data != data:
            curr = curr.next
        curr.next = curr.next.next
        curr.next.prev = curr

    def display(self, head):
        curr = head
        print("null", end = " <=> ")
        while curr != None:
            print(curr.data,end=" <=> ")
            curr = curr.next
        print("null")

list1 = DLL()
list1.insert_at_front(66)
list1.insert_at_end(11)
list1.insert_at_end(22)
list1.insert_at_end(33)
list1.insert_at_front(44)
list1.insert_at_end(55)
list1.display(list1.head)
list1.delete(11)
list1.display(list1.head)