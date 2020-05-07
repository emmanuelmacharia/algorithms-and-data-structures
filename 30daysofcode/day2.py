'''
Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

'''


def sumSquares(num):
    ''' get the total of the individual numbers first '''
    result = 0
    while num:
        result += (num % 10)**2
        num = num // 10
    return result


def isHappyNumber(n):
    # import pdb
    # pdb.set_trace()
    myset = set()
    myset.add(n)
    result = 0
    while True:
        num = sumSquares(n)
        if num == 1:
            result = num
            break
        elif num in myset:
            result = num
            break
        else:
            myset.add(num)
            result = num
            n = num
            continue

    return myset, result == 1, result


print(isHappyNumber(19763529748))
