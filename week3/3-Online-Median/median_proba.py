# this script checks if median.py is callable externally and if it works well
import sys, os, random
if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())
from median import Median
    
instance = Median
while True:
  instr = input('insert ')
  if instr == 'exit':
    break
  else:
    print(instance.insert(int(instr)))

# the program doesn't misbehave
