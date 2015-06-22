class Vector: 
    global array
    array = [1, 2, 15, None, None]
    
    # Adds value at a specific index in the Vector.
    # Complexity: O(n)
    def insert(index, value):
        Vector.expand()
        if index > array.index(None)-1 or index > len(array)-1:
            Vector.add(value)
        else:

            array.insert(index, value)
            array.remove(None)
            Vector.expand()
        pass

    # Adds value to the end of the Vector.
    # Complexity: O(1)
    def add(value):
        array[array.index(None)] = value
        Vector.expand()
        pass

    # Returns value at a specific index in the Vector
    # Complexity: O(1)
    def get(index):
        return array[index]
        pass

    # Removes element at the specific index
    # Complexity: O(n)
    def remove(index):
        array.remove(array[index])
        array.append(None)
        Vector.shrink()
        return array
        pass

    # Removes element at the last index
    # Complexity: O(1)
    def pop():
        temp = array[array.index(None)-1]
        array[array.index(None)-1] = None
        Vector.shrink()
        return temp
        pass

    # Returns the number of elements in the Vector.
    # Complexity: O(1)
    def size():
        return array.index(None)
        pass

    # Returns the total capacity of the Vector.
    # Complexity: O(1)
    def capacity():
        return len(array)
        pass

    # expand array capacity if it is full
    def expand():
        if None not in array:
            for x in range(len(array)):
                array.append(None)

    # shrink array capacity if vector is too enough
    def shrink():
        global array
        if array.index(None) < 0.35*len(array) and len(array) > 5:
            array = array[:int(len(array)/2)]
