class Roots:
    # Finds the square root of a number using binary search.
    # number - int
    def square_root(n):
        low = 0.0
        upp = n
        mid = low +(upp - low)/2
        while True:
            if mid*mid > n:
                upp = mid
            else:
                low = mid
            last = mid
            mid = (upp+low)/2
            if abs(mid-last) < 0.00000000000001:
                break
        return '%.5f' % mid
        pass

inp = input('')
res = str(Roots.square_root(int(inp)))

print (res)
