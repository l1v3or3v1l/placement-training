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

    def length(self):
        l = 0
        curr = self.head
        while curr != None:
            curr = curr.next
            l += 1
        return l
    
    def insert_at_front(self, data):
        new = Node(data)
        if self.head != None:
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
    
    def delete(self, data):    
        temp = self.head
        if temp.data == data:
            self.head = temp.next
        else:
            while temp.next.data != data:
                temp = temp.next
            print(temp.data)
            temp.next = temp.next.next

    # Reversing a Linked List
    # prev is set to None
    # curr is set to head
    # till curr is None,
    #   next is set to next node of curr
    #   the bond next to curr is broken and attached to the previous Node (prev)
    #   eg. 23 <-- 11 -x-> 21
    #      prev   curr    next
    #   prev is then set to curr and curr to next (moving one step ahead)
    # finally prev would be pointing to the first node of reversed list (head)

    def reverse(self):
        prev = None
        curr = self.head
        while curr != None:
            next = curr.next
            curr.next = prev
            prev, curr = curr, next
        return prev


ll = SLL()
ll.insert_at_end(10)
ll.insert_at_front(11)
ll.insert_at_front(22)
ll.insert_at_front(33)
ll.insert_at_end(44)
ll.insert_at_end(55)
ll.display(ll.head)
ll.delete(55)
ll.display(ll.head)
new_head = ll.reverse()
ll.display(new_head)