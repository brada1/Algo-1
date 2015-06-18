from collections import Counter
class Quadruplets:

    # Returns the number of quadruplets that sum to zero.
    # a - [int]
    # b - [int]
    # c - [int]
    # d - [int]
    # worst = O(n^2 logn)
    def zero_quadruplets_count(a, b, c, d):
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
        pass
