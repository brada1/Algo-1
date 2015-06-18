# test random numbers
import sys, os, random
if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())
from phone_book import PhoneBook
phones = random.sample (range(20), 10)
names = ['bradan', 'petkan', 'parastas', 'sex phone', 'satanata',
         'neo', 'baba matka', 'kolio gol', 'jo kulta', 'bob brown']
book = [None]*len(names)
for i in range(len(names)):
    book[i] = (phones[i], names[i])
    print (book[i])
book = sorted(book)
print ('sort it:')
for i in range(len(book)):
    print (book[i])
numbers = random.sample(range(20), 3)
print ('search for', numbers)

#test examples
##book = [(1, "Stanislav"), (15, "Rado"), (6, "Ivan"), (8, "Ivan")]
##numbers = [15, 8]

pb = PhoneBook
print (pb.lookup_names(book, numbers))
