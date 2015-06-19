# O(n^2 logn) - store sum of a[i]+b[j] in ab[]*(len(a)*len(b)) and
# c[k]+d[l] in cd[]*(len(c)*len(d))
# then index out both arrays two obtain unique values
# sort cd
# perform binary search on cd for every element in ab
# if bin search is successful increase count by the occurances in ab times
# the occurances in cd
from collections import Counter
def quadFour(a, b, c, d):
    ab = [i+j for i in a for j in b]
    cd = [-(k+l) for k in c for l in d]
    ab = Counter(ab).most_common()
    cd = Counter(cd).most_common()
    cd = sorted(cd)
    count = 0
    for i in range(len(ab)):
        lo = 0
        hi = len(cd)-1
        while lo <= hi:
            m = lo
            if cd[m][0] == ab[i][0]:
                count += cd[m][1]*ab[i][1]
                break
            else:
                if cd[m][0] <= ab[i][0]:
                    lo += 1
                else:
                    hi -= 1
    return count
