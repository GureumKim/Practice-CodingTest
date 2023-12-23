from sys import stdin; input = stdin.readline
from collections import deque

# 이어졌는 지 끊겼는지 체크를
# 한 사이클이 지나면 계속, 계속 해줘야 함!!

def grouping(y,x,arr,v):

    parts = deque()
    parts.append((y,x))
    v[y][x] = 1

    while parts:
        y,x = parts.popleft()
        for di, dj in [(0,1),(1,0),(0,-1),(-1,0)]:
            dy,dx = y +di, x +dj
            if arr[dy][dx] and not v[dy][dx]:
                v[dy][dx] = 1
                parts.append((dy,dx))

    return 1

def solve(n,m,arr):
    melted = deque()
    time = 0

    while True:
        visited = [[0] * m for _ in range(n)]
        for i in range(1,n-1):
            for j in range(1,m-1):
                if arr[i][j] == 0: continue
                cnt = 0
                for di, dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                    dy, dx = i+di, j+dj
                    if arr[dy][dx] == 0:
                        cnt +=1
                if cnt:
                    melted.append((i,j,cnt))

        while melted:
            y,x, d = melted.popleft()
            arr[y][x] = max(0,arr[y][x]-d)

        group = 0
        for i in range(1,n-1):
            for j in range(1,m-1):
                if arr[i][j] and not visited[i][j]:
                    group += grouping(i,j,arr,visited)
                if group > 1:
                    return time+1

        if group == 0:
            return 0

        time += 1

if __name__ == "__main__":
    n,m = map(int,input().split())
    area = [list(map(int,input().split())) for _ in range(n)]
    print(solve(n,m,area))