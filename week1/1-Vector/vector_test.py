# test if vector.py is callable externally and if it works well
import sys, os
if os.getcwd() not in sys.path:
        sys.path.append(os.getcwd())
from vector import Vector

# run-time loopy
instr = 1
while instr > 0:
    instr = int(input('(0)EXIT\n(1)INSERT\n(2)ADD\n(3)GET\n(4)REMOVE\n(5)POP\n(6)SIZE\n(7)CAPACITY\n'))
    if instr == 1:
        ind = int(input('Index?\n'))
        val = input ('Value?\n')
        print (Vector.insert(ind, val))
    elif instr == 2:
        val = input ('Value?\n')
        print (Vector.add(val))
    elif instr == 3:
        ind = int(input('Index?\n'))
        print (Vector.get(ind))
    elif instr == 4:
        ind = int(input('Index?\n'))
        print (Vector.remove(ind))
    elif instr == 5:
        print (Vector.pop())
    elif instr == 6:
        print (Vector.size())
    elif instr == 7:
        print (Vector.capacity())
