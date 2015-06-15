print ('Benchmarking sorting algorithms...')
# import necessary modules from necessary folders
import random, time, sys, os
if os.getcwd() not in sys.path:
        sys.path.append(os.getcwd())
from selects import selectSort
from insert import insertSort
from merge import mergeSort
from quick import quickSort
from count import countSort

n = 5                                                   # highest order(+1) of array size
m = 7                                                   # repeat m times for averaging
times = [[0 for f in range(6)] for f in range(n-1)]     # initialize benchmark matrix
begin = time.clock()                                    # initialize timing of whole operation

def dup(alist, arr):
        '''make an element by element duplicate of the random array'''
        for x in range(0, len(arr)):
                alist[x] = arr[x]
        return alist

def setin(i, end, a):
        '''modify benchmark matrix with most recent value at current position'''
        times[i-1][a] = (times[i-1][a] + end)/2

# operation repetition (to take avarages of benchmark times)
for z in range(0, m):
        # repetition for different orders of array size
        for i in range(1,n):    
                
                l = 10**i                                               # order of array size
                arr = [int(random.random()*100) for j in range(l)]      # create an array of random numbers with incremental order
                alist = [0]*len(arr)                                    # initialize an empty array of same size
                times[i-1][0] = l                                       # add the order as the first column in the matrix

                # a loop to go through all the sorting algorithms
                for g in range(1, 6):                                   
                        start = time.clock()                            # get a CPU clock tick
                        if g == 1:
                                temp = selectSort(dup(alist, arr))
                        elif g == 2:
                                temp = insertSort(dup(alist, arr))
                        elif g == 3:
                                temp = mergeSort(dup(alist, arr))
                        elif g == 4:
                                temp = quickSort(dup(alist, arr))
                        elif g == 5:
                                temp = countSort(dup(alist, arr))
                        end = time.clock() - start                       # get a CPU clock tick and estimate algorithm r
                        setin(i, end, g)

endit = time.clock() - begin                                             # estimate overal calculation time
print ('Total time Elapsed:', endit, 'seconds.') 

# show the benchmark table
for i in range(0, n-1):
        print (times[i])
