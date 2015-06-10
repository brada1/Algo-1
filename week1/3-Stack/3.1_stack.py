# init a small stack
stack = [None]*6
for i in range(0, 3):
    stack[i] = i + 1
print (stack, '\n')


class Stack:
    def __init__(self, stack):
        self.result = stack

    def push(self, stack):
        if None not in stack:
            for i in range (0, len(stack)):
                stack.append (None)
        if stack[0] == None:
            stack[0] = 1
        else:
            stack[stack.index(None)] = stack[stack.index(None)-1] + 1
        self.result = stack

    def pop(self, stack):
        if stack.index(None) < 0.35*len(stack) and len(stack) > 3:
            stack = stack[:int(len(stack)/2)]
        stack[stack.index(None)-1] = None
        self.result = stack

    def peek(self, stack):
        print (stack[stack.index(None)-1])

    def size(self, stack):
        print (stack[stack.index(None)-1])

#run-time loop
ins = 0
while ins >= 0:
    ins = int(input('(1)PUSH\n(2)POP\n(3)PEEK\n(4)SIZE\n(5)EXIT\n'))
    s = Stack(stack)
    if ins == 1:
        s.push(stack)
    elif ins == 2:
        s.pop(stack)
    elif ins == 3:
        s.peek(stack)
        continue
    elif ins == 4:
        s.size(stack)
        continue
    elif ins == 5:
        break
    stack = s.result
    print (stack, '\n')
