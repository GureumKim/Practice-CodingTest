from collections import deque
from sys import stdin; input= stdin.readline
def rgblind(si,sj):
    q = deque()
    q.append((si,sj))
    checked_rbl[si][sj] = 1
    color = pic[si][sj]
    while q:
        y,x = q.popleft()
        for di, dj in [(1,0),(0,1),(-1,0),(0,-1)]:
            dy, dx = y+di, x+dj
            if 0<=dy<n and 0<=dx<n and not checked_rbl[dy][dx]:
                if color == 'B':
                    if pic[dy][dx] == 'B':
                        checked_rbl[dy][dx] = 2
                        q.append((dy,dx))
                else:
                    if pic[dy][dx] in ['R','G']:
                        checked_rbl[dy][dx] = 1
                        q.append((dy,dx))
    return 1
def normal(si,sj):
    q = deque()
    q.append((si,sj))
    checked[si][sj] = 1
    color = pic[si][sj]

    while q:
        y,x = q.popleft()
        for di, dj in [(1,0),(0,1),(-1,0),(0,-1)]:
            dy, dx = y+di, x+dj
            if 0<=dy<n and 0<=dx<n and not checked[dy][dx]:
                if color == pic[dy][dx]:
                    checked[dy][dx] = color
                    q.append((dy,dx))
    return 1

n = int(input())
pic = [list(input().rstrip()) for _ in range(n)]
checked_rbl = [[0] * n for _ in range(n)]
checked = [[0] * n for _ in range(n)]
rbl_cnt, cnt = 0, 0

for i in range(n):
    for j in range(n):
        if not checked_rbl[i][j]:
            rbl_cnt += rgblind(i,j)
        if not checked[i][j]:
            cnt += normal(i,j)
print(cnt,  rbl_cnt)