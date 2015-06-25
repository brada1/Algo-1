from heapq import heappush, heappop

class Median:
  #upper is a min heap of the numbers which are larger than the median
  #lower is a max heap of the numbers which are smaller than the median
  #to construct a max heap, heapq is used with negative input
  global upper, lower
  upper, lower = [], []
  
  #inserts the number and returns the median
  def insert(number):
    if len(lower) == 0 or number < -lower[0]:
      heappush(lower, -number)
    else:
      heappush(upper, number)

    # rebalance the heaps by ensuring that their lengths are different by 1 element at most
    if len(upper) - len(lower) > 1:
      heappush(lower, -heappop(upper))
    elif len(lower) - len(upper) > 1:
      heappush(upper, -heappop(lower))

    # get the median (the root of either lower or upper)
    if len(lower) > len(upper):
      return -lower[0]
    else:
      return upper[0]

# Thanks to Khoa Tran
