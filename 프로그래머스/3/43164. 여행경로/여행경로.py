def solution(tickets):
    from collections import defaultdict
    import heapq
    answer = []
    
    airports = defaultdict(list)
    
    for start, end in tickets:
        heapq.heappush(airports[start], end)
    
    stack = ['ICN']
    
    # 꼭 연결되게 가야 되는 게 아니라
    # 모든 티켓을 이용해서, 모든 도시를 방문하면 되는 거임
    # 하나의 네트워크로 경로를 연결시키라는 조건은 없음!!!
    while stack:
        while airports[stack[-1]]:
            stack.append(heapq.heappop(airports[stack[-1]]))
        answer.append(stack.pop())
    
    return answer[::-1]