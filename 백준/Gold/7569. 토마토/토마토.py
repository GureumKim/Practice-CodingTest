from sys import stdin; input = stdin.readline
from collections import deque


def bfs(st, left):
    q = deque()
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if st[k][i][j] == 1:
                    q.append((j, i, k, 0))
                    left -= 1
                elif st[k][i][j] == -1:
                    left -= 1

    if left == 0: return 0

    while q:
        x, y, z, day = q.popleft()

        for dk in direct_z:
            dz = z + dk
            if 0 > dz or h <= dz or st[dz][y][x]: continue
            st[dz][y][x] = 1
            left -= 1
            q.append((x, y, dz, day + 1))

        for di, dj in direct_xy:
            dy, dx = y + di, x + dj
            if 0 <= dy < n and 0 <= dx < m and st[z][dy][dx] == 0:
                st[z][dy][dx] = 1
                left -= 1
                q.append((dx, dy, z, day + 1))

        # left 확인을 여기서 해야 분기가 깔끔함
        # 처음 left가 0 이면 이미 return 0을 했기 때문
        if left == 0:
            return day + 1

    return -1


if __name__ == "__main__":
    m, n, h = map(int, input().split())

    storage = [list(list(map(int, input().split())) for _ in range(n)) for _ in range(h)]

    direct_xy = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    direct_z = [-1, 1]

    print(bfs(storage, m * n * h))