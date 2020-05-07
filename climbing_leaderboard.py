
def climbingLeaderboard(scores, alice):
    '''returns alice's score upon every game she plays'''
    myset = set([])
    for i in range(0, len(alice)):
        # print(alice[i])
        scores.append(alice[i])
        for o in scores:
            # print(f'this here is o ===> {o}')
            myset.add(o)
            # print(f'this here is myset ====> {myset}')
        iterlist = sorted(list(myset), reverse=True)
        for x in iterlist:
            print(f'heres x ===> {x} and heres alice[i] ==> {alice[i]}')
            if x == alice[i]:
                print(iterlist.index(x))
            else:
                continue


scores, alice = [100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102]
climbingLeaderboard(scores, alice)

# [list((i, test_list[i])) for i in range(len(test_list))]
