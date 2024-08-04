def solution(scoville, K):
    import heapq as hq
    hq.heapify(scoville)
    answer = 0
    
    while True:
        a = hq.heappop(scoville)
        if a >= K:
            return answer
        if not scoville:
            return -1
            
        b = hq.heappop(scoville)
        answer += 1
        hq.heappush(scoville, a + 2 * b)