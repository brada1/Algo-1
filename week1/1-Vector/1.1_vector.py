# initiate by creating an array where capacity is size doubled
siz = int(input('Create a vector of size?\n'))
vec = ['neshto'] * siz
for x in range(0, siz):
    vec.append(None)
print (vec, '\n')

# double the capacity of needed
def sizcheck(siz, vec):
    if siz == len(vec):
        for x in range(0, siz):
            vec.append(None)        
        
# insertion in vector (not at end) and removal of one empty space of capacity
def ins(siz, vec):
    ind = int(input('Choose index for insertion (must be less than ' + str(siz) + '):\n'))
    c = 0
    while c != -1:
        if ind > siz - 1:
            ind = int(input('index is outside of vector size, repeat\n' ))
        else:
            sizcheck(siz, vec)
            val = input('The value of the element would be:\n')
            vec.insert(ind, val)
            vec.remove(None)
            print (vec, '\n')
            c = -1

# append to end of vector
def app(siz, vec):
    sizcheck(siz, vec)
    val = input('The value of the element would be:\n')
    vec[siz] = val
    print (vec, '\n')

# show the value at a specific index (less than or equal to the size of the vector)
def get(siz, vec):
    ind = int(input('Choose index to show its value:\n'))
    c = 0
    while c != -1:
        if ind > siz -1:
            ind = int(input('Index is outside of vector size, repeat:\n' ))
        else:
            print (vec[ind], '\n')
            c = -1

# run-time loopy
instr = 0
while instr >= 0:
    instr = int(input('Choose instruction:\n(1) INSERT\n(2) APPEND TO END\n(3) GET VALUE AT INDEX\n(4) GET SIZE\n(5) GET TOTAL CAPACITY\n(6) EXIT\n'))

    if instr == 1:
        ins(siz, vec)
        siz = siz + 1
    elif instr == 2:
        app(siz, vec)
        siz = siz + 1
    elif instr == 3:
        get(siz, vec)
    elif instr == 4:
        print ('The vector size is: ', siz, '.\n')
    elif instr == 5:
        print ('The vector capacity is: ', len(vec), '.\n')
    elif instr == 6:
        break
    else:
        print ('Come again?')
        
    
