from sys import stdin; input = stdin.readline
from collections import deque

def min_dist():
    # global mn

    q = deque()
    # y, x, dist, chance
    q.append((0,0,1,1))
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1

    while q:
        y,x, dist, chance = q.popleft()
        if y==n-1 and x==m-1:
            return dist
        for di, dj in [(0,1),(1,0),(0,-1),(-1,0)]:
            dy, dx = y+di, x+dj
            if not (0<=dy<n) or not (0<=dx<m): continue

            if chance:
                if visited[dy][dx] == 1: continue
                # 다음 changce 있는 상태에서 방문하면 벽을 이미 먼저 뚫었으니까 체크
                # 앞으로는 길이 똑같을 텐데(0만 갈 수 있음, 미리 방문했으니까)
                # chance 없는 상태에서 방문하면 이미 방문한 곳이니까 체크

                # 한 번 벽 뚫어도 끝까지 못갈 수 있으니
                # chance 있을 때 없을 때 visited에 1,2 값 넣어서 분기
                visited[dy][dx] = 1
                if map_[dy][dx] == 0:
                    q.append((dy,dx,dist+1,1))
                else:
                    q.append((dy,dx,dist+1,0))

            else:
                # 방문한적이 없어야하고, 이미 방문했으면 당연히 벽 안뚫은 애들보다
                # 같거나 늦을 수 밖에 없음
                if visited[dy][dx] == 0 and map_[dy][dx] == 0:
                    # 벽 뚫으면 당연히 벽 안뚫고 간 것보다 같거나 빨리 갈 수 밖에 없음
                    visited[dy][dx] = 2
                    q.append((dy,dx,dist+1,0))

    # 일단 쨌든 벽 부셔서 바로 도착할 때가 가장 적은 dist일 거기 때문에
    # while 끝나고 분기 안해도 될듯..?
    return -1

n, m = map(int,input().split())
map_ = [list(map(int,input().rstrip())) for _ in range(n)]
ans = min_dist()
print(ans)