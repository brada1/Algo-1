# test if vector.py is callable externally and if it works well
import sys, os
if os.getcwd() not in sys.path:
        sys.path.append(os.getcwd())
from stack import Stack

ins = 1
while ins > 0:
    ins = int(input('(0)EXIT\n(1)PUSH\n(2)POP\n(3)PEEK\n(4)SIZE\n'))
    if ins == 1:
        val = input('Value?\n')
        print (Stack.push(val))
    elif ins == 2:
        print (Stack.pop())
    elif ins == 3:
        print (Stack.peek())
    elif ins == 4:
        print (Stack.size())
