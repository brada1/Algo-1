# initiate by creating an array where capacity is size doubled
siz = int(input('Create a vector of size?\n'))
vec = ['neshto'] * siz
for x in range(0, siz+1):
    vec.append(None)
print (vec, '\n')

class Check:
    def __init__(self, vec):
        self.resultch = vec

    def enlarge(self, vec):
        if None not in vec:
            for x in range(0, len(vec)):
                vec.append(None)

class Vector:
    def __init__(self, vec):
        self.result = vec

# insertion in vector (not at end) and removal of one empty space of capacity
    def insert(self, vec):
        chins = Check(vec)
        chins.enlarge(vec)
        ind = int(input('Choose index for insertion (must be less than ' + str(vec.index(None)) + '):\n'))
        c = 0
        while c != -1:
            if ind > vec.index(None)-1:
                ind = int(input('index is outside of vector size, repeat\n' ))
            else:
                chins = Check(vec)
                chins.enlarge(vec)
                val = input('The value of the element would be:\n')
                vec.insert(ind, val)
                vec.remove(None)
                print (vec, '\n')
                c = -1

# append to end of vector
    def add(self, vec):
        chapp = Check(vec)
        chapp.enlarge(vec)
        val = input('The value of the element would be:\n')
        vec[vec.index(None)] = val
        print (vec, '\n')

# show the value at a specific index (less than or equal to the size of the vector)
    def get(self, vec):
        ind = int(input('Choose index to show its value:\n'))
        c = 0
        while c != -1:
            if ind > siz -1:
                ind = int(input('Index is outside of vector size, repeat:\n' ))
            else:
                print (vec[ind], '\n')
                c = -1

    def size(self, vec):
        print ('The vector size is: ' + str(vec.index(None)) + '.\n')

    def capacity(self, vec):
        print ('The vector capacity is: ' + str(len(vec)) + '.\n')
# run-time loopy
instr = 1
while instr > 0:
    instr = int(input('(0)EXIT\n(1)INSERT\n(2)ADD\n(3)GET\n(4)SIZE\n(5)CAPACITY\n'))
    v = Vector(vec)
    if instr == 1:
        v.insert(vec)
    elif instr == 2:
        v.add(vec)
    elif instr == 3:
        v.get(vec)
    elif instr == 4:
        v.size(vec)
    elif instr == 5:
        v.capacity(vec)
    
