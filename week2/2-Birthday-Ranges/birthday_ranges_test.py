import sys, os, random
if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())
from birthday_ranges import BirthdayRanges

#test example
birthdays = [5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15]
ranges = [(4, 9), (6, 7), (200, 225), (300, 365)]

# test sequential array
##birthdays = [3, 4, 5, 6, 7, 8 ,9 ,10, 11]
##ranges = [[0, 5],
##          [4, 9],
##          [8, 15]
##          ]

# test pseudo-random array (not unique values)
##bds = [int(random.random()*365) for i in range(10)]
##print (bds, 'random array')
##birthdays = sorted(bds)
##ranges = [0]*3
##for j in range(3):
##    rang = [int(random.random()*365) for k in range(2)]
##    if rang[0] > rang [1]:
##        tmp = rang[0]
##        rang[0] = rang[1]
##        rang[1] = tmp
##    ranges[j] = rang
    
print (birthdays, 'sorted random array')



bdr = BirthdayRanges
print (bdr.birthdays_count(birthdays, ranges))


