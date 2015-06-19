# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html

class Merge:
    
    def sort(alist):
        if len(alist)>1:
            mid = len(alist)//2
            lefthalf = alist[:mid]
            righthalf = alist[mid:]

            Merge.sort(lefthalf)
            Merge.sort(righthalf)

            i=0
            j=0
            k=0
            while i<len(lefthalf) and j<len(righthalf):
                if lefthalf[i]<righthalf[j]:
                    alist[k]=lefthalf[i]
                    i=i+1
                else:
                    alist[k]=righthalf[j]
                    j=j+1
                k=k+1

            while i<len(lefthalf):
                alist[k]=lefthalf[i]
                i=i+1
                k=k+1

            while j<len(righthalf):
                alist[k]=righthalf[j]
                j=j+1
                k=k+1
            return alist

