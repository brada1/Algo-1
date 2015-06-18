# O(n^3) - replace the last 2 loops with left-right linear traversal (or smthn)

def quadThree(a, b, c, d):
    c = sorted(c)
    d = sorted(d)
    count = 0
    cl = len(c)
    dl = len(d)
    for i in range(len(a)):
        for j in range(len(b)):
            l = 0
            r = dl - 1
            while l < cl and r >= 0:
                s = a[i] + b[j] + c[l] + d[r]
                if s == 0:
                    #print (a[i], b[j], c[l], d[r])
                    count += 1
                    l += 1
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
    return count

