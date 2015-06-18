# O(n^3 logn) - replace innermost loop with binary search

def quadTwo(a, b, c, d):
    # sort d so that binary search can be implemented
    d = sorted(d)
    count = 0
    for i in range(len(a)):
        for j in range(len(b)):
            for k in range(len(c)):
                su = -(a[i]+b[j]+c[k])
                # binary search the d vector
                l = 0
                r = len(d)-1
                while l <= r:
                    m = l
                    if d[m] == su:
                        #print (a[i], b[j], c[k], d[l])
                        count += 1
                        break
                    else:
                        if d[m] <= su:
                            l += 1
                        else:
                            r -= 1
    return count

