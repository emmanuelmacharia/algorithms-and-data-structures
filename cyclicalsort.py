'''given an array that is cyclicly sorted; find the index of the smallest element of the array

eg: a = [4,5,6,7,1,2,3]
returns 4


'''


def findSmallest(array):
    for a in range(len(array)):
        if a == 0 or a == len(array):
            pass
        elif array[a - 1] > array[a] < array[a + 1]:
            return a


a = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
print(
    f"so here is the index of he smallest integer: {findSmallest(a)} and this is the value of the smallest integer: {a[findSmallest(a)]}")
