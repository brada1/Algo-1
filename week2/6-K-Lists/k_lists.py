class Node:

    def value():
        pass

    def next():
        pass

class KLists:

    # Merge K sorted lists using a heavily modified counting sort.
    # Count sort is a lot faster than heap sort, so this method should be
    # faster than implementing a heap.
    def merge(lists):
        # the length of the list containing the count of occurances...
        # of each unique value is the maximum(last) value of all lists
        mah = 0
        for i in range(len(lists)):
            if lists[i][len(lists[i])-1] > mah:
                mah = lists[i][len(lists[i])-1]
            else:
                mah = mah
        count_list = [0]*(mah+1)
        
        # make a histogram of the frequency of occurances of a given value
        for i in range(len(lists)):
            for j in range(len(lists[i])):
                count_list[lists[i][j]] += 1

        # calculate starting index for each value
        total = 0
        for i in range(mah+1):
            oldCount = count_list[i]
            count_list[i] = total
            total += oldCount

        # the length of the ouput list is the
        # sum of the lengths of the input lists
        rl = 0
        for i in range(len(lists)):
            rl += len(lists[i])
        result = [0]*rl

        # copy to ouput list while preserving
        # order of inputs with equal values
        for i in range(len(lists)):
            for j in range(len(lists[i])):
                result[count_list[lists[i][j]]] = lists[i][j]
                count_list[lists[i][j]] += 1
        return result
