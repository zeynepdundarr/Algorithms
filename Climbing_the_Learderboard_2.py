


def climbing(rank_arr, player_arr):

    rank_arr = sorted(list(set(rank_arr)), reverse = True)

    j = 0
    l = len(rank_arr)
    res = []
    for el in player_arr:
        j = 0
        while j<l and el < rank_arr[j]:
            j += 1
        res.append(j+1)
    return res


    # find a place to Alice in learderboard
    # check if Alice's score is less than any ith element in rank board
    # while it is less than ith element go next
    # if it is not less 
    # rank is (i+1)

    # 1, 2, 3, 4 
    # 
    # fin
if __name__ == "__main__":

    a = input()
    a2 = input()
    a_arr = list(map(int, a2.split()))
    
    b = input()
    b2 = input()
    b_arr = list(map(int, b2.split()))
    
    res = climbing(a_arr, b_arr)
    #print(res)

    for i in res:
        print(i)


