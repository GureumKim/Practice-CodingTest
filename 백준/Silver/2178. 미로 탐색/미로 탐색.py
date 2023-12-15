from sys import stdin; input= stdin.readline
from collections import deque

n, m = map(int,input().split())
maze = [input().rstrip() for _ in range(n)]
# 불필요한 중복 막기 위해 visited 배열로 check
visited = [[0]*m for _ in range(n)]
# print(maze)

q = deque()
q.append((0,0,1))
visited[0][0] = 1

while q:
    y,x,cell = q.popleft()
    # print(f"y:{y} x:{x}")
    if y==n-1 and x==m-1:
        print(cell)
        break

    for di,dj in [(0,1),(1,0),(0,-1),(-1,0)]:
        dy, dx = y+di, x+dj
        if 0<=dy<n and 0<=dx<m and not visited[dy][dx] and maze[dy][dx]=='1':
            visited[dy][dx]=1
            q.append((dy,dx,cell+1))