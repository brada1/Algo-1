import sys, os
if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())
from heap_sort import HeapSort

class KMin:

    # Finds the k-th minimum element in an unsorted collection.
    # numbers - [int]
    # k - int
    
    def kthMinimum(numbers, k):
        heap = numbers[:k]
        itera = numbers[k:]
        if len(itera) == 0:
            heap = HeapSort.sort(heap)
        else:
            for i in range(len(itera)):
                heap = HeapSort.sort(heap)
                if heap[len(heap)-1] > itera[i]:
                    heap[len(heap)-1] = itera[i]
        return heap[len(heap)-1]
