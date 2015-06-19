#http://interactivepython.org/runestone/static/pythonds/SortSearch/TheSelectionSort.html

class SelectionSort:
   # Sorts a sequence of integers.
   def sort(sequence):
      """ sort by selection """
      for fillslot in range(len(sequence)-1,0,-1):
          positionOfMax=0
          for location in range(1,fillslot+1):
              if sequence[location]>sequence[positionOfMax]:
                  positionOfMax = location

          temp = sequence[fillslot]
          sequence[fillslot] = sequence[positionOfMax]
          sequence[positionOfMax] = temp
      return sequence

##seq = [4, 13, 52, 7, 18, 3, 1, 6]
##print (SelectionSort.sort(seq))
