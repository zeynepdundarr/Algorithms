
dict_rank = {}
player_rank = []

def climbing(rank_arr, player_arr):

    i = 0
    for player_val in player_arr:
        
        print("\n\n----------")
        print("Iter: ", i)
        print("Rank array: ", rank_arr)
        print("Player_val: ", player_val)
        print("----------")
        update_rank_array(rank_arr, player_val)
        i += 1

    print("Player rank is: ", player_rank)
    return player_rank

def update_rank_array(rank_arr, player_val):
    rank_arr.append(player_val)
    rank_arr.sort(reverse=True)
    print("Sorted rank array: ", rank_arr)
    get_ranks_from_scores(rank_arr)
    return get_player_rank(player_val)


def get_ranks_from_scores(rank_arr):

    # rank = 0, because rank array is sorted as descending
    global rank
    global dict_rank 
    dict_rank = {}
    rank = 0
    for el in rank_arr:
        print()
        print("El: ", el)
        print("Values: ", dict_rank.keys())
        if el not in dict_rank.keys():   
            rank += 1   
            dict_rank[el] = rank
            print("Rank is: ", rank)
            print() 
        else: 
            print("Rank is: ", rank)
            print()
            dict_rank[el] = rank
   

def get_player_rank(player_val):

    global dict_rank
    global player_rank
    for item in dict_rank.items():
        if item[0] == player_val:
            player_rank.append(item[1])
    print("Rank dict is: ", dict_rank)


if __name__ == "__main__":

    # a = int(input())
    # a_arr = list(map(int, a.split()))
    
    # b = int(input())
    # b_arr = list(map(int, b.split()))
    a_arr = [100, 90, 90, 80, 75, 60]
    b_arr = [50, 65, 77, 90, 102]
          
    # a_arr = [100, 100, 50, 40, 40, 20, 10] 
    # b_arr = [5, 25, 50, 120]
 


    res = climbing(a_arr, b_arr)
    #print(res)

    for i in res:
        print(i)


