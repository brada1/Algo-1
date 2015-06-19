class CountSort:
    # Sorts a sequence of integers.
    def sort(sequence):
        """in-place counting sort"""
        m = max(sequence) + 1
        count = [0] * m               # init with zeros
        for a in sequence:
            count[a] += 1             # count occurences
        i = 0
        for a in range(m):            # emit
            for c in range(count[a]): # - emit 'count[a]' copies of 'a'
                sequence[i] = a
                i += 1
        return (sequence)

##seq = [4, 13, 52, 7, 18, 3, 1, 6]
##print (CountSort.sort(seq))
