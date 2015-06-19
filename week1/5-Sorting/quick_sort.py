# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheQuickSort.html

class QuickSort:
   # Sorts a sequence of integers.
   def sort(sequence):
      """perform quick sort"""
      QuickSort.quickSortHelper(sequence,0,len(sequence)-1)
      return (sequence)

   def quickSortHelper(alist,first,last):
      if first<last:

          splitpoint = QuickSort.partition(alist,first,last)

          QuickSort.quickSortHelper(alist,first,splitpoint-1)
          QuickSort.quickSortHelper(alist,splitpoint+1,last)


   def partition(alist,first,last):
      pivotvalue = alist[first]

      leftmark = first+1
      rightmark = last

      done = False
      while not done:

          while leftmark <= rightmark and \
                  alist[leftmark] <= pivotvalue:
              leftmark = leftmark + 1

          while alist[rightmark] >= pivotvalue and \
                  rightmark >= leftmark:
              rightmark = rightmark -1

          if rightmark < leftmark:
              done = True
          else:
              temp = alist[leftmark]
              alist[leftmark] = alist[rightmark]
              alist[rightmark] = temp

      temp = alist[first]
      alist[first] = alist[rightmark]
      alist[rightmark] = temp


      return rightmark

seq = [4, 13, 52, 7, 18, 3, 1, 6]
print (QuickSort.sort(seq))

