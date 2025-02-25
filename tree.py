# height is for a tree
# depth is for a specific node
# complete binary tree
#   only after filling a level can you move to next level
#   only can fill from left to right
# full binary tree
#   every node should have either 0 or 2 children
# inorder traversal = Left Root Right
# preorder traversal = Root Left Right
# postorder traversal = Left Right Root
# binary search tree = inorder traversal is sorted

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

def preorder_traversal(node):
    if node:
        print(node.data, end = " ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)

preorder_traversal(root)
print("Preorder")

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.data, end = " ")
        inorder_traversal(node.right)


inorder_traversal(root)
print("Inorder")

def postorder_traversal(node):
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.data, end = " ")

postorder_traversal(root)
print("Postorder")

from collections import deque

def level_order_traversal(node):
    if not node:
        return
    queue = deque([node])
    while queue:
        current = queue.popleft()
        print(current.data, end = " ")
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

level_order_traversal(root)
print("Levelorder")

def is_complete(node):
    if not node:
        return True
    queue = deque([node])
    reached_end = False
    while queue:
        curr = queue.popleft()
        if curr is None:
            reached_end = True
        else:
            if reached_end:
                return False
            queue.append(curr.left)
            queue.append(curr.right)
    return True

print(is_complete(root))

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(5)
root.right.left = Node(5)

print(is_complete(root))

def find_height_edges(node):
    if not node:
        return -1
    left_height = find_height_edges(node.left)
    right_height = find_height_edges(node.right)
    return max(left_height, right_height) + 1

print(find_height_edges(root))

def find_height_nodes(node):
    if not node:
        return 0
    left_height = find_height_nodes(node.left)
    right_height = find_height_nodes(node.right)
    return max(left_height, right_height) + 1

print(find_height_nodes(root))