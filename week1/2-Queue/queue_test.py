# test if queue.py is callable externally and if it works well
import sys, os
if os.getcwd() not in sys.path:
        sys.path.append(os.getcwd())

from queue import Queue

print (Queue.size())
# main loopy-droopy
##instr = 1
##while instr > 0:
##    instr = int(input('(0)EXIT\n(1)PUSH\n(2)POP\n(3)PEEK\n(4)SIZE\n'))
##    if instr == 1:     
##        val = input('Value?\n')
##        print (Queue.push(val))
##    elif instr == 2:
##        print (Queue.pop())
##    elif instr == 3:
##        print (Queue.peek())
##    elif instr == 4:
##        print (Queue.size())
