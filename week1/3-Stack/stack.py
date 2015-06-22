class Stack:
    global array
    array = [None]*5

    # Adds value to the end of the Stack.
    # Complexity: O(1)
    def push(value):
        if array[0] == None:
            array[0] = value
        else:
            array[array.index(None)] = value
        Stack.expand()
        return array
        pass

    # Returns value from the end of the Stack and removes it.
    # Complexity: O(1)
    def pop():
        temp = array[array.index(None)-1]
        array[array.index(None)-1] = None
        Stack.shrink()
        return temp
        pass

    # Returns value from the end of the Stack without removing it.
    # Complexity: O(1)
    def peek():
        return array[array.index(None)-1]
        pass

    # Returns the number of elements in the Stack.
    # Complexity: O(1)
    def size():
        return array.index(None)
        pass

    def expand():
        if None not in array:
            for x in range(len(array)):
                array.append(None)

    def shrink():
        global array
        if array.index(None) < 0.35*len(array) and len(array) > 5:
            array = array[:int(len(array)/2)]
