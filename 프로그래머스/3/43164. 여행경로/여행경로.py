def solution(tickets):
    from collections import defaultdict
    import heapq
    answer = []
    
    airports = defaultdict(list)
    
    for start, end in tickets:
        heapq.heappush(airports[start], end)
    
    stack = ['ICN']
    
    while stack:
        while airports[stack[-1]]:
            stack.append(heapq.heappop(airports[stack[-1]]))
        answer.append(stack.pop())
    
    return answer[::-1]