# O(n^4)
def quadOne(a, b, c, d):
    count = 0
    for i in range(len(a)):
        for j in range(len(b)):
            for k in range(len(c)):
                for l in range(len(d)):
                    su = a[i] + b[j] + c[k] + d[l]
                    if su == 0:
                        #print (a[i], b[j], c[k], d[l])
                        count += 1
    return count
