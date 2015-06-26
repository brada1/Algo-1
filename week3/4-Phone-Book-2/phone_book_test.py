# this script checks if phone_book.py is callable externally and if it works well
import sys, os, random
if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())
from phone_book import PhoneBook

# this works in Sublime and IDLE
mytree = PhoneBook()
mytree.insert('brada', 15654)
mytree.insert('laino', 2651)
mytree.insert('nqkoi', 255225)
mytree.insert('sjieets', 25252553)
mytree.insert('kotui', 3)
mytree.insert('kokojambo', 6)
mytree.remove('kotui')
mytree.remove('nqkoi')
mytree.insert('brada', 2)


print(mytree.lookup('pesho'))
print(mytree.lookup('brada'))
mytree.list()

# this works in IDLE for the most part
# pb = PhoneBook()
# instr = ''
# while True:
#     instr = input('')
#     if instr == 'exit':
#      break
#     else:
#      if instr == 'list':
#        pb.list()
#      if ' ' in instr:
#        split = instr.split()
#        operation = split[0]
#        if operation == 'insert':
#          pb.insert(split[1], split[2])
#        elif operation == 'lookup':
#          print(pb.lookup(split[1]))
#        elif operation == 'remove':
#          pb.remove(split[1])