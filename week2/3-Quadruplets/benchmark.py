import sys, os, random, time
if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())

##a = [5, 3, 4]
##b = [-2, -1, 6]
##c = [-1, -2, 4]
##d = [-1, -2, 7]
for y in range(1, 5):
    brada = y*10
    a = random.sample(range(-brada*2, brada*2), brada)
    b = random.sample(range(-brada*2, brada*2), brada)
    c = random.sample(range(-brada*2, brada*2), brada)
    d = random.sample(range(-brada*2, brada*2), brada)

    from quadone import quadOne
    s = time.clock()
    qone = quadOne(a, b, c, d)
    sone = round(time.clock() - s,4)

    from quadtwo import quadTwo
    s = time.clock()
    qtwo = quadTwo(a, b, c, d)
    stwo = round(time.clock() - s,4)

    from quadthree import quadThree
    s = time.clock()
    qthree = quadThree(a, b, c, d)
    sthree = round(time.clock() - s,4)

    from quadfour import quadFour
    s = time.clock()
    qfour = quadFour(a, b, c, d)
    sfour = round(time.clock() - s,4)
    
    if qone == qtwo == qthree == qfour:
        print (brada, sone, stwo, sthree, sfour)
    else:
        print (qone, qtwo, qthree, qfour)
