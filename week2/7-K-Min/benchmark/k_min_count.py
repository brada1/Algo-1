from collections import Counter

class Kmin:

    def kthM(numbers, k):
        numbers = Counter(numbers).most_common()
        numbers = sorted(numbers)

        return numbers[k-1][0]
