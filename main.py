# from functools import reduce
# import operator


# class Solution:
#     '''
#     rearranges the numbers in the list to the next greater permutations of the number
#     if there's no such available arrangement, you should return a sorted list
#     the replacements must also be in place; no .remove/.pop/.append
#     '''

#     def nextPermutation(self, nums):
#         '''the base method called that initiates the checks in the class'''

#         # check whether its a len(list)=1 list to avoid out of bound errors later on
#         if len(nums) == 1:
#             return nums

#         split = self.get_split(nums)

#         if split == -1:
#             nums.sort()
#             return nums
#         else:
#             change_index = self.get_largest(nums, split)
#             self.swap(nums, split, change_index)
#             self.reverse(nums, split + 1)

#     def get_split(self, nums):
#         '''this finds the index to which the larger index is found when comparing every two'''
#         i = len(nums) - 1
#         while i >= 0:
#             if nums[i] <= nums[i - 1]:
#                 i -= 1
#             else:
#                 break
#         return i - 1

#     def get_largest(self, nums, i):
#         '''find the largest int in the list'''
#         j = len(nums) - 1
#         while j > i and j >= 0:
#             if nums[j] > nums[i]:
#                 break
#             else:
#                 j -= 1
#         return j

#     def swap(self, nums, i, j):
#         '''does the swapping in the array'''
#         nums[i], nums[j] = (nums[j], nums[i])

#     def reverse(self, nums, begin):
#         '''
#         reverses the integers where begin is what the int on the left
#         and end is the one on the right. We call swap from here to swap the integers
#         '''
#         start = begin
#         end = len(nums) - 1
#         while start < end:
#             self.swap(nums, start, end)
#             start += 1
#             end -= 1


# x = Solution()
# lsit = [2, 2, 0, 2, 2]
# print(x.nextPermutation(lsit))


# # def get_split(nums):
# #     i = len(nums) - 1
# #     while i >= 0:
# #         if nums[i] < nums[i - 1]:
# #             i -= 1
# #         else:
# #             break
# #     return i - 1


# # def get_largest(nums, i):
# #     j = len(nums) - 1
# #     while j >= i:
# #         if nums[j] > nums[i]:
# #             break
# #         else:
# #             j -= 1
# #     return j


# # def swap(nums, i, j):
# #     nums[i], nums[j] = (nums[j], nums[i])


# # def reverse(nums, begin):
# #     start = begin
# #     end = len(nums) - 1
# #     while start < end:
# #         swap(nums, start, end)
# #         start += 1
# #         end -= 1


# # def lex(myList):
# #     '''
# #     rearranges the numbers in the list to the next greater permutations of the number
# #     if there's no such available arrangement, you should return a sorted list
# #     the replacements must also be in place; no .remove/.pop/.append
# #     '''
# #     split = get_split(myList)

# #     if split == -1:
# #         myList.sort()
# #         return myList
# #     else:
# #         change_index = get_largest(myList, split)
# #         swap(myList, split, change_index)
# #         reverse(myList, split + 1)


# # lis = [5, 1, 1]
# # print(lex(lis))


'''reverse an integer'''


def reverser(x):
    my_Str = str(x)
    reversedInt = 0
    modulus = 10
    if x < 0:
        iterator = len(my_Str) - 1
        m = x * -1
    else:
        iterator = len(my_Str)
        m = x

    while iterator != 0:
        reversedInt = reversedInt * 10
        reversedInt = reversedInt + m % modulus
        m //= modulus
        iterator -= 1
    if x < 0:
        return reversedInt * -1
    return reversedInt


print(reverser(-321))
