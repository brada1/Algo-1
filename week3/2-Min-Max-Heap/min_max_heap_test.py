import sys, os
if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())
from min_max_heap import MinMaxHeap

mm_heap = [8, 71, 41, 31, 10, 11, 16, 46, 51, 31, 21, 13]
not_mm_heap = [8, 71, 41, 31, 10, 11, 99999, 46, 51, 31, 21, 13]

print (MinMaxHeap.isMinMax(mm_heap))     
print (MinMaxHeap.isMinMax(not_mm_heap))
