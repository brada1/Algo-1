#http://interactivepython.org/runestone/static/pythonds/SortSearch/TheInsertionSort.html

class InsertionSort:
   # Sorts a sequence of integers.
   def sort(sequence):
      """ sort by indrtion """
      for index in range(1,len(sequence)):

        currentvalue = sequence[index]
        position = index

        while position>0 and sequence[position-1]>currentvalue:
            sequence[position]=sequence[position-1]
            position = position-1

        sequence[position]=currentvalue
      return sequence
     
##seq = [4, 13, 52, 7, 18, 3, 1, 6]
##print (InsertionSort.sort(seq))
