from collections import deque

def bfs(y,x):
    b_q = deque()
    b_q.append((y,x,0))
    visited = [[0]*c for _ in range(r)]
    visited[y][x] = 1

    # 물 다 차기 전에 어떻게든 먼저 도착하거나
    # 고슴도치가 못 가는 상황 나올 것
    while b_q:
        # water 시작되는 곳의 개수가 유동적임
        # 매번 확인 필요
        # print(len(water))
        for _ in range(len(water)):
            wy, wx = water.popleft()
            for di, dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                dwy, dwx = wy+di, wx+dj
                if dwy<0 or dwy>=r or dwx<0 or dwx>=c: continue
                if map_[dwy][dwx] in ['.','S']:
                    map_[dwy][dwx] = '*'
                    water.append((dwy,dwx))

        # for i in range(r):
        #     print(*map_[i])

        for _ in range(len(b_q)):
            sy, sx, time = b_q.popleft()
            # print("time",time)
            for di, dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                dsy, dsx = sy+di, sx+dj
                if 0<=dsy<r and 0<=dsx<c and not visited[dsy][dsx]:
                    if map_[dsy][dsx] == 'D':
                        return time+1
                    elif map_[dsy][dsx] == '.':
                        # print(f"y:{dsy} x:{dsx}\n")
                        b_q.append((dsy,dsx,time+1))
                        visited[dsy][dsx] = 1
            # print(len(b_q))
            # print(b_q)

    return "KAKTUS"

r, c = map(int,input().split())
map_ = [list(input()) for _ in range(r)]
# print(map_)
water = deque()
rock = []
by, bx = None, None
for i in range(r):
    for j in range(c):
        if map_[i][j] == 'S':
            by, bx = i, j
        elif map_[i][j] == '*':
            water.append((i,j))

print(bfs(by,bx))