'''
    Given n array of integers, find the longest subset array that is a subsequence
    and the XOR between the integers within the subsequence is equal to k and return its length
    eg.
        Input:        
            arr = [2,1,3,4,5,2]
            k = 2
        Output:
            sub = [1,3]
            because 1 ^ 3 = k.
    Im assuming here that a subsequence is a list of integers that is sorted in ascending order
'''


def getXORSubsequence(n, arr, k):
    '''Given n array of integers, find the subset array that is a subsequence
    and the XOR between the integers within the subsequence is equal to k'''

    # create a map to store elements that are subsequent
    subdict = {}
    # an array to store elements who's XOR = k
    sub = []
    # another array to store the longest subsequent array
    res = []

    # iterate through your array to find subsequent integers
    for i in range(len(arr)):
        if i >= 1:
            if arr[i - 1] <= arr[i]:
                # if they are subsequent,
                # add them to an array value, with the iterator as the key to the dictionary(map)
                subdict[i] = [arr[i-1], arr[i]]
                # import pdb; pdb.set_trace()
            else:
                res.append([arr[i - 1], arr[i]])
    # print(f'here we have res ===> {res}')

    # iterate through the map to check their XOR values of individual subsequent sub arrays
    for key in subdict:
        for i in range(len(subdict[key])):
            if i == 1:
                if subdict[key][i] ^ subdict[key][i-1] == k:
                    # if their XOR is equal to k, append them to sub
                    try:
                        sub.append(subdict[key])
                        print(f'here we have sub {sub}')
                    except Exception as e:
                        print(e)
            else:
                continue

    # iterate through sub to try create the longest
    #  subsequent array of integers who's XOR is equal to K ie. res
    for a in range(len(sub)):
        if a >= 1:
            if sub[a-1][-1] == sub[a][0]:
                res = sub[a-1].append(sub[a][1])
            else:
                res.append(sub[a])

    # find the longest array in res and return that!
    result = len(max(res, key=len))
    return result


arr1 = [1, 1, 1]  # 3
arr = [1, 2, 2, 1, 3]  # 1
n = len(arr)
k = 5
print(getXORSubsequence(n, arr, k))

# NOTES:
#    Im not sure on the time and space complexity of this function;
#    I tried splitting it out to reduce nested for-loops, to reduce on time complexities
#    When it comes to space complexity, im creating 3 new data structures; 2 arrays and one map;
#    would love if there was a way to optimize it, maybe try out a linked list; that would be awesome
#    Lastly, im not sure what happens if the array doesnt have a sequence who's XOR == k;
#    they arent clear about that case and what they meant when they said that you can return a one-item array
