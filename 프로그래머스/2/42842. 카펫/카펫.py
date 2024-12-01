def solution(brown, yellow):
    answer = []
    
    yellow_w_plus_h = (brown - 4) / 2
    
    sieve = [True] * (yellow + 1)
    sieve[0] = False
    
    for i in range(2, int(yellow ** 0.5) + 1):
        if yellow % i:
            sieve[i] = False
    
    for h in range(1, int(yellow ** 0.5) + 1):
        if sieve[h]:
            w = yellow / h
            if w + h == yellow_w_plus_h and w * h == yellow:
                answer = [w + 2, h + 2]
    
    return answer