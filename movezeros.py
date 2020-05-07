'''given an array with n elements, write a function that moves all zeros to the end of the array; do it in place'''


def moveZeroes(arr):
    indexOfZero = []
    for i in arr:

        if i == 0:
            indexOfZero.append(arr.index(i))
        else:
            pass

    x = len(indexOfZero)
    print(f'whats indexOfZero? => {indexOfZero}')
    while x > 0:

        for y in range(len(indexOfZero)):
            print(f"whats y => {y}")
            print(f'array => {arr}')
            arr.remove(indexOfZero[y])
            print(f'arr after removing => {arr}')
            arr.append(indexOfZero[y])

        x -= 1
    return arr


print(moveZeroes([2, 0]))
