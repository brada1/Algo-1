class Heap:

    # Sorts a sequence of integers by heap sort.
    def sort(sequence):
        for s in range(int((len(sequence)-2)/2), -1, -1):
            siftdown(sequence, s, len(sequence)-1)

        for e in range(len(sequence)-1, 0 ,-1):
            sequence[e], sequence[0] = sequence[0], sequence[e]
            siftdown(sequence, 0, e - 1)
        return sequence
        pass


def siftdown(lst, s, e):
    r = s
    while True:
        c = r*2 + 1
        if c > e: break
        if c+1 <= e and lst[c] < lst[c+1]:
            c += 1
        if lst[r] < lst[c]:
            lst[r], lst[c] = lst[c], lst[r]
            r = c
        else:
            break


