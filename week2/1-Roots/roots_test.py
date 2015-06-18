import sys, os
if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())
from roots import Roots
n = 4

while n != 'exit':
    n = input("Type a number.\n")
    if n == 'exit':
        break
    else:
        sr = Roots
        print ('sqrt(', str(n), ') = ', round(sr.square_root(float(n)),5))
