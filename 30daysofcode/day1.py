'''Given a non-empty array of integers, every element appears twice except for one. Find that single one.'''


def singleton(arr):
    '''
    finds the single element in the array

    Uses the XOR operator where n ^ n = 0 and n ^ 0 = n
    therefore, every duplicating number's XOR will equal 0 
    and the result will equal the unique number

    '''
    import pdb
    pdb.set_trace()
    result = 0

    for i in arr:
        result = result ^ i

    return result


myarr = [4, 1, 2, 1, 2]
print(f'heres using xor {singleton(myarr)}')


def singleton2(arr):
    myset = set(arr)
    return (2 * sum(myset) - sum(arr))


print(f'heres using the sum {singleton2(myarr)}')
