def solution(maps):
    from collections import deque    
    
    n, m = len(maps), len(maps[0])
    queue = deque()
    queue.append((0,0,1)) # (y,x,ans)
    maps[0][0] = -1 # 지나간 곳은 -1
    
    dir = [(1,0), (0,1), (-1,0), (0,-1)]
    
    while queue:
        y, x, ans = queue.popleft()
        if y == n-1 and x == m-1:
            return ans
        for dy, dx in dir:
            y_, x_ = y + dy, x + dx
            if 0 <= y_ < n and 0 <= x_ < m and maps[y_][x_] == 1:
                maps[y_][x_] = -1
                queue.append((y_, x_, ans+1))
            
    
    return -1