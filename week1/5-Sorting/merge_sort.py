# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html

class MergeSort:
    # Sorts a sequence of integers.
    def sort(sequence):
        """ perform a merge sort """
        if len(sequence)>1:
            mid = len(sequence)//2
            lefthalf = sequence[:mid]
            righthalf = sequence[mid:]

            MergeSort.sort(lefthalf)
            MergeSort.sort(righthalf)

            i=0
            j=0
            k=0
            while i<len(lefthalf) and j<len(righthalf):
                if lefthalf[i]<righthalf[j]:
                    sequence[k]=lefthalf[i]
                    i=i+1
                else:
                    sequence[k]=righthalf[j]
                    j=j+1
                k=k+1

            while i<len(lefthalf):
                sequence[k]=lefthalf[i]
                i=i+1
                k=k+1

            while j<len(righthalf):
                sequence[k]=righthalf[j]
                j=j+1
                k=k+1
            return sequence
        
##seq = [4, 13, 52, 7, 18, 3, 1, 6]
##print (MergeSort.sort(seq))
