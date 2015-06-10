# init a small stack
stack = [None]*6
for i in range(0, 3):
    stack[i] = i + 1
print (stack, '\n')

# run-time loop
ins = 0
while ins >= 0:
    ins = int(input('(1)PUSH\n(2)POP\n(3)PEEK\n(4)SIZE\n(5)EXIT\n'))
# PUSH ================================================================
    if ins == 1:
        if None not in stack:
            for i in range (0, len(stack)):
                stack.append (None)
        if stack[0] == None:
            stack[0] = 1
        else:
            stack[stack.index(None)] = stack[stack.index(None)-1] + 1
        print (stack, '\n')

# POP =================================================================
    elif ins == 2:
        if stack.index(None) < 0.35*len(stack) and len(stack) > 3:
            stack = stack[:int(len(stack)/2)]
        stack[stack.index(None)-1] = None
        print (stack, '\n')

# PEEK & SIZE (it's an integer stack starting with 1 [easy]) ==========
    elif ins == 3 or ins == 4:
        print (stack[stack.index(None)-1])

# EXIT ================================================================
    elif ins == 5:
        break