def solution(scoville, K):
    import heapq
    heapq.heapify(scoville)
    answer = 0
    l = len(scoville)
    
    while l > 1:
        a = heapq.heappop(scoville)
        if a >= K:
            break
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a+b*2)
        answer += 1
        l -= 1
    
    else:
        if heapq.heappop(scoville) < K:
            answer = -1
    
    return answer