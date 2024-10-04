def solution(n, edge):
    from collections import deque
    
    def bfs():
        q = deque()
        q.append((1, 0)) # node, dist
        visited[1] = True
        
        while q:
            node, dist = q.popleft()
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    res[neighbor] = dist + 1
                    q.append((neighbor, dist + 1))
    
    adj = [[] for _ in range(n + 1)]
    for n1, n2 in edge:
        adj[n1].append(n2)
        adj[n2].append(n1)
    
    visited = [False] * (n + 1) 
    res = [0] * (n + 1)
    bfs()
    
    mx = max(res[2:])
    ans = 0
    for i in range(2, n + 1):
        if res[i] == mx:
            ans += 1
    return ans