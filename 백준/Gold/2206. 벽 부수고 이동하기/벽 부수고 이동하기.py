"""
벽 뚫게 되면 도착 점 가지 못하더라도
visited 배열에 흔적이 남음
left = 0 일 때와 아직 left 있을 때를 나눠서
visited 배열에 표시하는 것이 중요 포인트!
"""
from sys import stdin; input = stdin.readline
from collections import deque
def bfs():
    q = deque()
    q.append((1,0,0,1)) # sy,sx,dist,left
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1

    while q:
        dist,y,x,left = q.popleft()
        if y == n-1 and x == m-1:
            return dist
        for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            dy, dx = y+di, x+dj
            if 0<=dy<n and 0<=dx<m:
                if left:
                    if visited[dy][dx] == 1:continue
                    visited[dy][dx] = 1
                    if map_[dy][dx] == 0:
                        q.append((dist+1,dy,dx,left))
                    else:
                        q.append((dist+1,dy,dx,0))
                else:
                    if visited[dy][dx] == 0 and map_[dy][dx] == 0:
                        visited[dy][dx] = 2
                        q.append((dist+1,dy,dx,0))
    return -1

n,m = map(int,input().split())
map_ = [list(map(int,input().rstrip())) for _ in range(n)]
res = bfs()
print(res)