import sys

class BST:
    '''this class instantiates a tree and calls the isBST check '''
    def __init__(self):
        self.root = None

    def isBST(self):
        '''checks if the binary tree instance is a bst'''
        self.root.isBST()
        return result

    def insert(self, data):
        '''used to build a bst, refers to Node().insert for the most part'''
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

global last, result
result = True
last = -sys.maxsize
class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def isBST(self):
        '''performes an in-order traversal and check if the elements are sorted'''
        global last, result
        if self:
            if self.left:
                self.left.isBST()
            if self.value <= last:
                result = False
            last = self.value
            if self.right:
                self.right.isBST()
                
    def insert(self, data):
        '''does the heavy lifting of building a bst'''
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
