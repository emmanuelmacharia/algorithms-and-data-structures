'''
You are given an array of n integers and a number k. 
Determine whether there is a pair of elements in the array that sums to exactly k. 
For example, given the array [1, 3, 7] and k = 8, the answer is “yes,” but given k = 6 the answer is “no.” 
'''



def sumPair(arr, k):
    ''' Working here with the two pointer method'''
    sorted(arr);
    p1 = 0
    p2 = -1

    for i in range(len(arr)):
        if arr[p1] + arr[p2] == k:
            return (arr[p1], arr[p2], True)
        elif arr[p1] + arr[p2] > k:
            p2 -= 1
        elif arr[p1] + arr[p2] < k:
            p1 += 1
        else:
            return False


arr = [1,2,3,4,19,18,17]
k = 19

print(sumPair(arr, k))





'''
Sliding window-- 

Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
'''


def slidingWindow(arr, k):
    '''
    uses the sliding window approach to get the averages of contiguous subarrays
    '''
    start = 0
    subSum = 0
    subAverage = 0
    end = k
    myArr = []

    if k > len(arr):
        return myArr;
    
    for i in range(len(arr)):
        if end > len(arr) - 1:
            print(end, len(arr))
            return myArr
        else:
            subSum = sum(arr[start : end])
            subAverage = subSum / k
            myArr.append(subAverage)
            start += 1
            end += 1

    return myArr


arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5

print(slidingWindow(arr, k))



def findTriplets(arr, k):
    sorted(arr)
    p1 = 0
    p2 = 1
    p3 = 2
    result = []
    
    for i in range(len(arr)):
        if arr[p1] + arr[p2] + arr[p3] == 0:
            result.append([arr[p1], arr[p2], arr[p3]])







