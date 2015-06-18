import sys, os
if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())
from quadruplets import Quadruplets
a = [5, 3, 4]
b = [-2, -1, 6]
c = [-1, -2, 4]
d = [-1, -2, 7]

print (Quadruplets.zero_quadruplets_count(a, b, c, d))
