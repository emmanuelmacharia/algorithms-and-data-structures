"""
Given a matrix of m * n elements, return all elements of the matrix in spiral order

Example: [
    [1,2,3], 
    [4,5,6],
    [7,8,9]
]

returns [1,2,3,6,9,8,7,4,5]



[
    [1,2,3,4], 
    [5,6,7,8], 
    [9,10,11,12], 
    [13,14,15,16]
]

returns [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]
"""


def spiral(a):
    m = len(a[0]) #3
    n = len(a) #3
    top  = 0
    bottom = m - 1 #2
    left = 0
    right = n - 1 #2
    direction = 0
    myArr = []

    while top <= bottom and left <= right:
        if direction == 0:
            for i in range(left, right + 1):
                myArr.append(a[top][i])
            top += 1
            direction = 1
        elif direction == 1:
            for i in range(top, bottom + 1):
                myArr.append(a[i][right])
            right  -= 1
            direction = 2
        elif direction == 2:
            for i in range(right, left - 1 , -1):
                myArr.append(a[bottom][i])
            bottom -= 1
            direction = 3
        elif direction == 3:
            for i in range(bottom, top - 1 , -1):
                myArr.append(a[i][left])
            left += 1
            direction = 0

    return myArr

a  = [
    [1,2,3], 
    [4,5,6],
    [7,8,9]
]


b = [
    [1,2,3,4], 
    [5,6,7,8], 
    [9,10,11,12], 
    [13,14,15,16]
]

c = [
    [1]
    ]
print(spiral(b))
