from sys import stdin; input = stdin.readline
from collections import deque

# 중복 코드 모듈화해서 더 깔끔하게 할 수 있는 지 재고하기
# def move(y, x):
#     pass

def bfs(sy,sx,sd):
    q = deque()
    q.append((sy,sx,sd,1))
    area[sy][sx] = 3

    while q:
        y,x,d,cnt = q.popleft()
        # if area[y][x] == 0:
            # area[y][x] = 3
        flag = 0
        for di, dj in [(1,0),(0,1),(-1,0),(0,-1)]:
            dy, dx = y+di, x+dj
            if 0<=dy<n and 0<=dx<m and area[dy][dx] == 0:
                d = (d+3)%4
                flag = 1
                break

        if flag:
            if d == 0:
                if y-1>=0 and area[y-1][x]==0:
                    area[y-1][x] = 3
                    q.append((y-1,x,d,cnt+1))
                else:
                    q.append((y,x,d,cnt))
            elif d == 1:
                if x+1<m and area[y][x+1]==0:
                    area[y][x+1] = 3
                    q.append((y,x+1,d,cnt+1))
                else:
                    q.append((y,x,d,cnt))

            elif d==2:
                if y+1<n and area[y+1][x]==0:
                    area[y+1][x] = 3
                    q.append((y+1,x,d,cnt+1))
                else:
                    q.append((y,x,d,cnt))
            elif d==3:
                if x-1>=0 and area[y][x-1]==0:
                    area[y][x-1] = 3
                    q.append((y,x-1,d,cnt+1))
                else:
                    q.append((y,x,d,cnt))
        else:
            flag2 = 0
            if d == 0:
                if y+1<n and area[y+1][x] != 1:
                    flag2 = 1
                    q.append((y+1,x,d,cnt))
            elif d == 1:
                if x-1>=0 and area[y][x-1] !=1:
                    flag2 = 1
                    q.append((y,x-1,d,cnt))
            elif d== 2:
                if y-1>=0 and area[y-1][x] != 1:
                    flag2 =1
                    q.append((y-1,x,d,cnt))
            else:
                if x+1<m and area[y][x+1]!=1:
                    flag2 = 1
                    q.append((y,x+1,d,cnt))

            if flag2 == 0:
                return cnt

    return cnt

n, m = map(int,input().split())
r, c, d = map(int,input().split())
area = [list(map(int,input().split())) for _ in range(n)]

print(bfs(r,c,d))