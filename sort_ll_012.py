class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def display(self, head):
        curr = head
        while curr != None:
            print(curr.data, end = " -> ")
            curr = curr.next
        print("null")
    
    def insert_at_end(self, data):
        new = Node(data)
        if self.head == None:
            self.head = new
        else: 
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = new

ll = SLL()
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(0)
ll.insert_at_end(1)
ll.insert_at_end(0)
ll.insert_at_end(2)
ll.display(ll.head)

zero = one = two = 0

curr = ll.head
while curr != None:
    if curr.data == 0:
        zero += 1
    elif curr.data == 1:
        one += 1
    elif curr.data == 2:
        two += 1
    curr = curr.next
curr = ll.head

while zero != 0:
    curr.data = 0
    zero -= 1
    curr = curr.next
while one != 0:
    curr.data = 1
    one -= 1
    curr = curr.next
while two != 0:
    curr.data = 2
    two -= 1
    curr = curr.next

ll.display(ll.head)