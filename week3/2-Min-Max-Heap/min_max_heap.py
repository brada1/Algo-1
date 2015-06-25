import sys
class MinMaxHeap:

    # Checks if a binary tree is a min/max heap.
    # Operates on an input list which is presumably a heap
    # Solution is ugly because there are additional instructions
    # which are helpful in case of visualisation of the validation process
    def isMinMax(mm_heap):
        # determine number of levels
        ch = True
        i = 1
        while ch:
            leng = 0
            for j in range(i+1):
                leng += 2**j
            if leng >= len(mm_heap):
                rem = leng - len(mm_heap)
                ch = False   
            i += 1
        levels = i
        if levels % 2 == 0:
            dummy = sys.maxsize
        else: dummy = -sys.maxsize

        # add missing leaves to heap array for next step
        for i in range(rem):
            mm_heap.append(dummy)        
                
        heap = [None]*(levels+1) 
        for i in range(1, levels+1):
            heap[i] = [0]*(2**(i-1))
            for j in range(len(heap[i])):
                heap[i][j] = mm_heap[(2**(i-1))+j-1]

        for i in range(1, len(heap)):
            heap[i].insert(0, None)

        result = True
        for i in range(1, levels):
            for j in range(1, len(heap[i])):
                if i % 2 == 1:              #if level is odd
                    if heap[i][j] > heap[i+1][(2*j)-1] or heap[i][j] > heap[i+1][2*j]:
                        result = False
                        break
                else:                       # if level is even
                    if heap[i][j] < heap[i+1][(2*j)-1] or heap[i][j] < heap[i+1][2*j]:
                        result = False
                        break
        return result
        pass
