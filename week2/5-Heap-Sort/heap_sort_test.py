# this script tests if heap_sort.py is callable externally
import sys, os
if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())
from heap_sort import HeapSort

ar = [7, 6, 5, 9, 8, 4, 3, 1, 2, 0]
ar2 = [4, 13, 52, 7, 18, 3, 1, 6]

print (HeapSort.sort(ar))
print (HeapSort.sort(ar2))


