# implement the simplest way of selecting the k-th minimum
import sys, os, time, random
if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())

from k_min_count import Kmin
from k_min import KMin


##a = [5, 2, 3, 6, 1, 4]
##k = 6

for i in range(1,7):
    o = 10**i
    a = random.sample(range(o*2), o)
    k = int(random.random()*i*10) + 1


    s = time.clock()
    by_count = Kmin.kthM(a, k)
    ec = round(time.clock() - s, 5)
    
    t = time.clock()
    by_heap = KMin.kthMinimum(a, k)
    eh = round(time.clock() - t, 5)

    if by_count != by_heap:
        print ('ERROR')
    else:
        print (o, k, ec, eh)
