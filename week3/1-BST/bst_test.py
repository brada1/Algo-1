import sys, os, time
if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())
from bst import BST

# first form a bst
class Node:
    '''each node of the tree is kept as an instance of the class'''
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def insert(self, data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True

    def find(self, data):
        if self.value == data:
            return True
        elif self.value > data:
            if self.left:
                return self.keft.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.right.find(data)
            else:
                return False

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

bst = Tree()
for i in range(500):
    bst.insert(i)
 
print(BST.isBST(Node(0)))
print(BST.isBST2(Node(0)))
