# this script tests if K-Lists.py is callable externally and if it works well
import sys, os, random
if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())
from k_lists import KLists


# test example
##lists = [(3, 5, 7, 9), (2, 4, 6), (0, 1, 8, 10)]

# test lists with a few occurances of the same value
##lists = [(1, 3, 5, 7, 9), (2, 4, 6, 11), (0, 1, 5, 8, 8, 10), (0, 1)]

# test with a random number of lists with random length with random elements
lil = (2 + int(random.random()*5))
lists = [0]*lil
for i in range(lil):
    le = 2 + int(random.random()*10)
    li = [0]*le
    for j in range(le):
        li[j] = int(random.random()*100)
    
    lists[i] = sorted(li)

# print input and output
print (lists)
print (KLists.merge(lists))
