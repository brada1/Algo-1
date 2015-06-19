# compare the performace of heap sort agains the performance of other sorting algos
import sys, os, random, time
if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())
from heap import Heap
from count import Count
from quick import Quick
from merge import Merge

n = 9
for i in range(1, n):
    l = 10**i
    arr = [int(random.random()*100) for j in range(l)]

##    s = time.clock()
##    Heap.sort(arr)
##    e = round(time.clock() - s, 5)

    s = time.clock()
    Count.sort(arr)
    e = round(time.clock() - s, 5)

##    s = time.clock()
##    sorted(arr)
##    e = round(time.clock() - s, 5)

##    s = time.clock()
##    Quick.sort(arr)
##    e = round(time.clock() - s, 5)

##    s = time.clock()
##    Merge.sort(arr)
##    e = round(time.clock() - s, 5)
    
    print (e)
