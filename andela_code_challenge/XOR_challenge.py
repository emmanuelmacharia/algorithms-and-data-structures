'''
    Given n array of integers, find the longest subset array that is a subsequence
    and the XOR between the integers within the subsequence is equal to k and return its length
    eg.
        Input:        
            arr = [2,1,3,4,5,2]
            k = 2
        Output:
            sub = [1,3]
            res = 2
            because 1 ^ 3 = k.
    
'''

import pdb

def getXORSubsequence(n, arr, k):
    i = 0
    start, stop, result = 0, 0, []
    # pdb.set_trace()
    if n < 2:
        result.append(arr)
    else:
        while i < n:
            if i == 0:
                if arr[i] ^ arr[i + 1] == k:
                    start = i
                else:
                    pass
            elif 0 < i < n - 1:
                if arr[i - 1] ^ arr[i] == k or arr[i] ^ arr[i + 1] == k:
                    if arr[i - 1] ^ arr[i] != k and arr[i] ^ arr[i + 1] == k:
                        start = i
                    elif arr[i - 1] ^ arr[i] == k and arr[i] ^ arr[i + 1] != k:
                        stop = i + 1
                    else:
                        pass
                else:
                    start, stop = i, i+1
                    result.append(arr[start: stop])

                if stop:
                    result.append(arr[start:stop])
            elif i == n - 1:
                if arr[i - 1] ^ arr[i] == k:
                    stop = i + 1
                else:
                    pass
                result.append(arr[start:stop])

            i += 1

    return len(max(result, key=len))


arr2 = [1000000]  # 1
arr1 = [1, 1, 1]  # 3
arr = [1, 2, 2, 1, 3]  # 1
n = len(arr1)
m = len(arr)
o = len(arr2)
k = 1
print(getXORSubsequence(o, arr2, k))
