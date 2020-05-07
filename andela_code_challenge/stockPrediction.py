import pdb

# def predictAnswer(stockData, queries):
#     result = []


def predictAnswer(stockData, queries):
    # pdb.set_trace()
    pre, post = 0, 0
    result = []
    stockData.insert(0, 0)
    for i in range(len(queries)):
        first = stockData[1: queries[i]]
        first.reverse()
        last = stockData[queries[i]:]
        pivot = stockData[queries[i]]

        if len(first) < 1:
            pre = 0
            pass
        else:
            for l in range(len(first)):
                if pivot > first[l]:
                    pre = stockData.index(first[l])
                    break
                else:
                    pre = 0
        if len(last) < 1:
            post = 0
            pass
        else:
            for k in range(1, len(last) - 1):
                if pivot > last[k]:
                    post = stockData.index(last[k])
                    break
                else:
                    post = 0

        if pre == 0 and post == 0:
            result.append(-1)
        elif pre == 0:
            result.append(post)
        elif post == 0:
            result.append(pre)
        elif queries[i] - pre < post - queries[i]:
            result.append(pre)
        elif queries[i] - pre > post - queries[i]:
            result.append(post)
        else:
            result.append(pre)

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


print(predictAnswer(stocks, queries))
