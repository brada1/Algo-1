class BirthdayRanges:

    # Return a vector with the number of people born in the specific ranges.
    # birthdays - [int]
    # ranges - [(int, int)]
    def birthdays_count(birthdays, ranges):
        birthdays = sorted(birthdays)
        inr = [None]*len(ranges)
        for i in range(len(ranges)):
            # lower bound
            l = 0
            r = len(birthdays)-1
            while l < r:
                m = int(round((l +(r - l)/2)))
                if ranges[i][0] < birthdays[m]:
                    r = m - 1
                else:
                    l = m + 1
            d = l
            if birthdays[d-1] == ranges[i][0]:
                d = d - 1

            # upper bound
            l = 0
            r = len(birthdays)-1
            while l < r:
                m = int(round((l +(r - l)/2)))
                if ranges[i][1] >= birthdays[m]:
                    l = m + 1
                else:
                    r = m - 1
            u = l
            if u == len(birthdays)-1:
                u = u + 1
                
            inr[i] = len(birthdays[d:u])

        return inr
        pass
        
