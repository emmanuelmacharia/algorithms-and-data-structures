def plusMinus(arr):
    '''returns the ratio between the positives, negatives and zero elements in an array of integers'''
    negative, positive, zero, total = 0, 0, 0, 0
    result = []
    for i in arr:
        if i < 0:
            negative += 1
        elif i == 0:
            zero += 1
        else:
            positive += 1
    total = negative + positive + zero

    negativeproportion = negative/total
    zeroproportion = zero/total
    positiveproportion = 1 - (negativeproportion + zeroproportion)
    result.append(positiveproportion)
    result.append(negativeproportion)
    result.append(zeroproportion)
    return result


print(plusMinus([-4, 3, - 9, 0, 4, 1]))


# def staircase(n):
#     mystr, spaces, hashes = '', '', ''
#     i = n
#     j = 0
#     while i > 0:
#         j += 1
#         spaces = ' '*(i - 1)
#         hashes = '#'*j
#         mystr = spaces + hashes
#         print(mystr)
#         i -= 1


# staircase(5)