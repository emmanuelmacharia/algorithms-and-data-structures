'''
Say you have an array for which the ith element is the price of a given stock on day i.pp
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), 
design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
'''

import sys


class MaximumProfit:
    '''contains methods that calculate the maximum profit one would get given an array of stock-market prices'''

    def getMaxProfit(self, arr):
        lowest_index = 0
        max_profit = sys.maxsize
        lowest_price = 0

        for i in range(0, len(arr)):
            print(f"iterator ===> {i}")
            if arr[i] < max_profit:
                mystring = "we're in the if block; arr[i] is less than max profit"
                max_profit = arr[i]
                lowest_index = i
                print(mystring)
                print(
                    f"the maximum profit == {max_profit} and the lowest index is === {lowest_index}")
            elif arr[i] - arr[lowest_index] > max_profit:
                mystring = "we're in the elif block; the difference between arr[i] and arr[lowest_index] is greter than max profit"
                max_profit = arr[i] - arr[lowest_index]
                print(mystring)
                print(f"here's the max_profit ===> {max_profit}")
        return max_profit


x = MaximumProfit()
print(x.getMaxProfit([7, 1, 5, 3, 6, 4]))


# i = arr[0]                        i = arr[1]                          i = arr[2]                      i = arr[3]
# 1st iter = [23, 19, 30, 40]       1st iter = [19, 30, 40]             1st iter = [30, 40]             1st iter = [40]
# 2nd iter = [19, 30, 40]           2nd iter = [20, 30]                 2nd iter = [40]
# 3rd iter = [30, 40]               3rd iter = [40]
# 4rth iter= [40]
