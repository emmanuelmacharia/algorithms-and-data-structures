'''
given an array of integers, write the most optimal function that can find the second largest integer in that list
e.g. given [6,11,22,2,65,78,9,23], returns 65
'''
import heapq


x = [6, 11, 22, 2, 65, 78, 9, 23]
heapq.heapify(x)

print(x)
# def get_Second_largest_element(arr):
#     # myheap = heapq._heapify_max(arr)
#     # largest = []
#     i = 2
#     # while i > 0:
#     # big = heapq.heappop(myheap)
#     # i -= 1
#     # print(big)
#     print(heapq._heapify_max(arr))


def get_second_largest_int(arr):
    heapq._heapify_max(arr)
    second_largest = 0
    i = 2
    while i > 0:
        second_largest = heapq.heappop(arr)
        heapq._heapify_max(arr)
        i -= 1
    return second_largest


print(get_second_largest_int([6, 11, 22, 2, 65, 78, 9, 23]))
