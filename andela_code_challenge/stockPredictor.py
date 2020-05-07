import pdb


def stockPredictor(stockData, queries):
    # pdb.set_trace()
    pointer, result = 0, []
    forwardPass, backwardPass = 0, 0
    stockData.insert(False, 0)
    for q in queries:
        if q >= len(stockData):
            result.append(-1)
            continue
        else:
            pointer = stockData[q]

        if pointer == stockData[1]:
            forwardPass = 2
            while pointer <= stockData[forwardPass]:
                forwardPass += 1
            else:
                result.append(forwardPass)

        elif pointer == stockData[-1]:
            backwardPass = len(stockData) - 2
            while pointer < stockData[backwardPass]:
                backwardPass -= 1
            else:
                result.append(backwardPass)
        else:
            forwardPass = stockData.index(pointer) + 1
            backwardPass = stockData.index(pointer) - 1
            while backwardPass > 1 and forwardPass < len(stockData) - 1:
                if stockData[backwardPass] > pointer or stockData[forwardPass] > pointer:
                    if stockData[backwardPass] > pointer < stockData[forwardPass]:
                        forwardPass += 1
                        backwardPass -= 1
                    elif stockData[backwardPass] > pointer > stockData[forwardPass]:
                        result.append(forwardPass)
                        break
                    elif stockData[backwardPass] < pointer < stockData[forwardPass]:
                        result.append(backwardPass)
                        break
                else:
                    result.append(backwardPass)
                    break
            else:
                if backwardPass < 2:
                    mySubSet = stockData[forwardPass:]
                    for i in range(len(mySubSet)):
                        forwardPass += 1
                        if pointer > mySubSet[i]:
                            result.append(i)

                if forwardPass == len(stockData) - 1:
                    mySubSet = stockData[0:backwardPass]
                    for i in range(len(mySubSet)):
                        forwardPass -= 1
                        if pointer > mySubSet[i] and i != 0:
                            result.append(i)

                    result.append(-1)

    return result


queries = [3, 1, 8]
stocks = [5,
          6,
          8,
          4,
          9,
          10,
          8,
          3,
          6,
          4]

print(stockPredictor(stocks, queries))

# queries = [3, 1, 8]
stocks = [5,
          6,
          8,
          4,
          9,
          10,
          8,
          3,
          6,
          4]


# result_list = []
#  stockData.insert(0, 0)
#   N = len(stockData)
#    for i in range(len(queries)):
#         firstPart = stockData[1:queries[i]]
#         day1 = N
#         day2 = N
#     for j in range(len(firstPart)-1, -1, -1):
#         if(stockData[queries[i]] > firstPart[j]):
#             day1 = j+1
#             break
#         else:
#             day1 = N

#         secondPart = stockData[queries[i]+1:N-1]
#         for k in range(len(secondPart)):
#             if (stockData[queries[i]] > secondPart[k]):
#                 day2 = queries[i]+k+1
#                 break
#             else:
#                 day2 = N

#         day = min([day1, day2])
#         if(day == N):
#             day = -1
#             result_list.append(day)
#             print('Resultant is: ', result_list)
#     return result_list
