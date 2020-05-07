'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

hint 1 : In-place means we should not be allocating any space for extra array. But we are allowed to modify the existing array. However, as a first step, try coming up with a solution that makes use of additional space. For this problem as well, first apply the idea discussed using an additional array and the in-place solution will pop up eventually.

hint 2 :  A two-pointer approach could be helpful here. The idea would be to have one pointer for iterating the array and another pointer that just works on the non-zero elements of the array.

'''


def move_zeroes(arr):
    # import pdb
    # pdb.set_trace()

    for i in range(0, len(arr)):
        if arr[i] != 0:
            pass
        else:
            k = arr[i]
            arr.remove(k)
            arr.append(k)

    return arr


def move_zeroes2(arr):
    import pdb
    pdb.set_trace()
    count = 0

    for i in range(0, len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    while count < len(arr):
        arr[count] = 0
        count += 1
    return arr


# print(move_zeroes([1, 2, 3, 4, 0, 4, 5, 6, 7, 0, 9, 8, 7, 6]))
print(move_zeroes2([1, 2, 3, 4, 0, 4, 5, 6, 7, 0, 9, 8, 7, 6]))
