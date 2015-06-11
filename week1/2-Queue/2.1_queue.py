# initiate a queue
que = ['go6u', 'pe6u', 'sa6u',
       'to6u', 'mi6u', 'pi6u',
       None, None, None]
print (que, '\n')

class Que:
    def __init__(self, que):
        self.result = que

    def push(self, que):
        if None not in que:                 # if the array is full...
            for x in range(0, len(que)):    # ...double it in size
                que.append(None)

        name = input('Who?\n')              # ask for value to push
        que[que.index(None)] = name         # add the value at the end of the queue
        self.result = que

    def pop(self, que):
        if que.index(None) < 0.35*len(que): # if the array is only 35% full...
            if len(que) > 3:                # do not shrink if it is already too small
                que = que[:int(len(que)/2)] # ... and half it in length

        if que[0] == None:                  # do not pop if queue is empty
            print ('Que is empty.\n')
        else:
            print (que[0], '\n')            # get the value at the start of the queue
            que.remove(que[0])              # remove the value at the start of the queue
            que.append(None)                # add empty value at the end of the que...
        self.result = que                   # ... in order to preserve array length constant

    def peek(self, que):
        print (que[0], '\n')                # just get it

    def size(self, que):
        if None not in que:                 # if array is full...
            print (len(que))                # print its whole length
        else:                               # otherwise...
            print (que.index(None))         # print the number of elements up to the first empty one

# main loopy-droopy
instr = 1
while instr > 0:
    instr = int(input('(0)EXIT\n(1)PUSH\n(2)POP\n(3)PEEK\n(4)SIZE\n'))
    q = Que(que)

    if instr == 1:     
        q.push(que)
    elif instr == 2:
        q.pop(que)
    elif instr == 3:
        q.peek(que)
    elif instr == 4:
        q.size(que)

    que = q.result                          # modify the que object and...
    print (que, '\n')                       # ... print it each iteration