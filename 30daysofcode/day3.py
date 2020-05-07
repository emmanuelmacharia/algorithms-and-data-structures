'''
Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O( n ) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

import sys


def max_sub(arr):
    import pdb
    pdb.set_trace()
    best, current = -sys.maxsize, 0
    for i in arr:
        current = max(i, current + i)
        best = max(best, current)
    return best


print(max_sub([-2, -1, -3, -4, -1, -2, -1, -5, -4]))
