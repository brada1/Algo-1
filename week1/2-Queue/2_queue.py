# initiate a que
que = ['go6u', 'pe6u', 'sa6u',
       'to6u', 'mi6u', 'pi6u',
       None, None, None]
print (que, '\n')

# adding with a expansion of needed     
def add(que, name):
    if None not in que:
        for x in range(0, len(que)):
            que.append(None)
    
    que[que.index(None)] = name
    print (que, '\n')

# get the name of the first person and remove him from que
def getndel(que):
    if que[0] == None:
        print ('Que is empty.\n')
    else:
        print (que[0], '\n')
        que.remove(que[0])
        que.append(None)
    print (que, '\n')
    
# run-time loopy-droopy
instr = 0
while instr >= 0:
    instr = int(input('(1)ADD\n(2)GET\n(3)GET N DEL\n(4)HOW MANY PPL\n(5)EXIT\n'))
    if instr == 1:
        name = input('Who?\n')
        add(que, name)
    elif instr == 2:
        print (que[0], '\n')
    elif instr == 3:
        getndel(que)
    elif instr == 4:
        if None not in que:
            print (len(que))
        else:
            print (que.index(None))
    elif instr == 5:
        break