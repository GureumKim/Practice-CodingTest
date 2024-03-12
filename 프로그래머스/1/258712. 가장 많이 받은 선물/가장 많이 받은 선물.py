def solution(friends, gifts):
    def comp(a,b):
        if exchange_data[a][b] > exchange_data[b][a]:
            result[a] += 1
        elif exchange_data[a][b] < exchange_data[b][a]:
            result[b] += 1
        else:
            comp_idx(a,b)
            
        
            
    def comp_idx(a,b):
        if exchange_data[a][a] == exchange_data[b][b]:
            return
        elif exchange_data[a][a] > exchange_data[b][b]:
            result[a] += 1
        else:
            result[b] += 1
    
    
    num_of_friends = len(friends)
    
    friends_dict = dict()
    # friends' names are the key of the dict
    for i in range(num_of_friends):
        friends_dict[friends[i]] = i
        
    # exchange_data[idx][idx]는 선물 지수
    # 나머지는 exchange_data[giver][receiver], receiver에게 선물 몇 개 줬는지 저장
    exchange_data = [[0]*num_of_friends for _ in range(num_of_friends)]
       
    for g in gifts:
        giver, receiver = g.split()
        
        idx_g, idx_r = friends_dict[giver], friends_dict[receiver]
        exchange_data[idx_g][idx_r] += 1
        
        exchange_data[idx_g][idx_g] += 1
        exchange_data[idx_r][idx_r] -= 1
        
        
    result = [0]*num_of_friends
    
    # i+1으로 불필요한 연산 제거
    for i in range(num_of_friends):
        for j in range(i+1,num_of_friends):
            # n : 0 번 교환일 수도 있다!! (반례)
            if exchange_data[i][j] or exchange_data[j][i]:
                comp(i,j)
            else:
                comp_idx(i,j)
            
    
    answer = max(result)
        
    
    return answer