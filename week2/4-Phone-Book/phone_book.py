class PhoneBook:

  # Find the names of people based on their phone numbers.
  # phone_book - [(String, int)]
  # numbers - [int]
  def lookup_names(phone_book, numbers):
    phone_book = sorted(phone_book)
    result = [None]*len(numbers)
    for i in range(len(numbers)):
        l = 0
        r = len(phone_book)
        while l < r:
            m = int(round(l+(r-l)/2))
            if phone_book[m][0] == numbers[i]:
                result[i] = phone_book[m][1]
                break
            else:
                if phone_book[m][0] < numbers[i]:
                    l += 1
                else:
                    r -= 1    
    return result
