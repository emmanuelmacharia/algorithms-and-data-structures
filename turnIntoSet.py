myArr = [1, 2, 3, 4, 55, 6, 7, 8, 9, 2, 4, 6, 55]
myset = set()

for i in range(0, len(myArr)-1):
    if myArr[i+1] != myArr[i]:
        myset.add(myArr[i])
    else:
        continue

mySet = set(myArr)

if mySet == myset:
    print(True)
else:
    print(False)


print(f'myset from my iterations ===> {myset}')
print(f'myset from using the set() method ===> {set(myArr)}')
