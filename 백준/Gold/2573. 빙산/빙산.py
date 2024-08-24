from sys import stdin
input = stdin.readline
from collections import deque


def main():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    n, m = map(int, input().split())
    field = list(list(map(int, input().split())) for _ in range(n))
    glacier = deque()
    answer = 0

    def melt(glc: deque) -> deque:
        melted = []
        res = deque()

        while glc:
            y, x, t = glc.popleft()
            cnt = 0
            for k in range(4):
                ny, nx = y + dy[k], x + dx[k]
                if ny < 0 or nx < 0 or ny > n or nx > m: continue
                if field[ny][nx] == 0:
                    cnt += 1
            if field[y][x] - cnt > 0:
                res.append((y, x, field[y][x] - cnt))
                field[y][x] = field[y][x] - cnt
            else:
                melted.append((y, x))
        for i, j in melted:
            field[i][j] = 0
        return res

    def grouping(sy, sx):
        q = deque()
        q.append((sy, sx))
        visited[sy][sx] = True

        while q:
            y, x = q.popleft()
            for k in range(4):
                ny, nx = dy[k] + y, dx[k] + x
                if 1 <= ny < n-1 and 1 <= nx < m-1 and not visited[ny][nx] and field[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx))

    for i in range(1, n-1):
        for j in range(1, m-1):
            if field[i][j]:
                glacier.append((i, j, field[i][j]))

    while glacier:
        answer += 1
        glacier = melt(glacier)
        # for i in range(n):
        #     print(*field[i])
        visited = [[False] * m for _ in range(n)]

        group = 0
        for i in range(1, n-1):
            for j in range(1, m-1):
                if field[i][j] and not visited[i][j]:
                    grouping(i, j)
                    group += 1
                if group > 1:
                    print(answer)
                    return
    print(0)


if __name__ == "__main__":
    main()
