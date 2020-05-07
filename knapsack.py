'''
solution for the knapsack 0-1 problem using dynamic programming
proof is done through proving the basecase
'''

# w = array of weights
# v = array of values
# n = number of items (int)
# C = capacity of knapsack


def knapsack(w, v, n, C):
    # uncomment the pdb lines if you want to debug or see how it builds the table
    # type 'h' to see all commands you can use when debugging
    # or go to https://docs.python.org/3/library/pdb.html

    '''debugging'''
    # import pdb
    # pdb.set_trace()

    '''create a 2D array to store our values'''
    table = [[0]*(C+1) for i in range(n + 1)]
    results, item, capacity = [], n, C
    
    #fill the first row with 0
    for i in range(C):
        table[0][i] = 0

    '''we loop through the number of items here.'''
    for i in range(1, n+1):
        # whenever i == 0, then capacity should always be 0,
        # because you havent collected an item of any weight

        '''we loop through the capacities, from 0 to C'''
        for k in range(C+1):
            if w[i-1] > k:
                # checking whether the item fits in the capacity we currently are at
                table[i][k] = table[i-1][k]
                # take the solution from the previous row
            else:
                table[i][k] = max((v[i-1]+table[i-1][k-w[i-1]]), table[i-1][k])
                # find  the max between taking and not taking, that's what you add to your table
    print(table)

    '''lets find the items that optimally fill the knapsack'''
    while item > 0:
        if table[item][capacity] > table[item-1][capacity]:
            results.append(item)
            capacity = capacity - w[item - 1]
        item -= 1

    return results


print(knapsack([1, 2, 3], [4, 3, 5], 3, 5))
