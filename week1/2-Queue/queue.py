class Queue:
    global array
    array = ['go6u', 'pe6u', 'sa6u', 'to6u', 'mi6u', 'pi6u', None, None, None]
    
    # Adds value to the end of the Queue.
    # Complexity: O(1)
    def push(value):
        array[array.index(None)] = value
        Queue.expand()
        return array

    # Returns value from the front of the Queue and removes it.
    # Complexity: O(1)
    def pop():
        tmp = array[0]
        array.remove(que[0])
        array.append(None)
        Queue.shrink()
        return tmp

    # Returns value from the front of the Queue without removing it.
    # Complexity: O(1)
    def peek():
        return array[0]

    # Returns the number of elements in the Queue.
    # Complexity: O(1)
    def size():
        if None not in array:
            return len(array)
        else:
            return array.index(None)

    def expand():
        if None not in array:
            for x in range(len(array)):
                array.append(None)

    def shrink():
        if array.index(None) < 0.35*len(array) and len(array) > 5:
            array = array[:int(len(array)/2)]

##print (Queue.push(2))
