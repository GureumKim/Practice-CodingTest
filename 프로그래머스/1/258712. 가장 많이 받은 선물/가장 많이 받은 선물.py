def solution(friends, gifts):
    from collections import defaultdict
    answer = 0
    name = defaultdict(int)
    for i, f in enumerate(friends):
        name[f] = i
    
    give = [[0] * len(friends) for _ in range(len(friends))]
    receive = [[0] * len(friends) for _ in range(len(friends))]
    rate = [0] * len(friends)
    res = [0] * len(friends)
    
    for gift in gifts:
        g, r = gift.split()
        g, r = name[g], name[r]
        
        give[g][r] += 1
        receive[r][g] += 1
        rate[g] += 1
        rate[r] -= 1
        
    for i in range(len(friends)):
        for j in range(i+1, len(friends)):
            if give[i][j] == give[j][i]:
                if rate[i] > rate[j]:
                    res[i] += 1
                elif rate[i] < rate[j]:
                    res[j] += 1
                continue
            
            if give[i][j] > give[j][i]:
                res[i] += 1
            else:
                res[j] += 1
    
    answer = max(res)
    
    return answer