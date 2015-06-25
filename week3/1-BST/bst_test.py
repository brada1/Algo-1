# this script checks if bst.py is callable externally and if it works well
import sys, os, random
if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())
from bst import BST

bst = BST()
array = random.sample(range(0, 100), 10)
print (array)
for i in range(10):
    bst.insert(array[i])
    
print (bst.isBST())

