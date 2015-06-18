class Roots:
    # Finds the square root of a number using binary search.
    # number - int
    def square_root(n):
        sgn = 0
        if n < 0:
            n = -n
            sgn = -1
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
            if abs(mid-last) < 0.00001:
                break
        if sgn < 0:
            return complex(0, mid)
        return mid
        pass
