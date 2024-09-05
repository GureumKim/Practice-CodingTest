def main():
    from sys import stdin
    from collections import deque

    def bfs():
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        visited = [[0] * m for _ in range(n)]

        q = deque([(0, 0, 1, 1)])
        visited[0][0] = 2

        while q:
            y, x, chance, dist = q.popleft()
            if y == n - 1 and x == m - 1:
                return dist
            for k in range(4):
                ny, nx = y + dy[k], x + dx[k]
                if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] != 2:
                    if chance:
                        visited[ny][nx] = 2
                        if _map[ny][nx] == '1':
                            q.append((ny, nx, 0, dist + 1))
                        else:
                            q.append((ny, nx, chance, dist + 1))
                    else:
                        if _map[ny][nx] == '0' and visited[ny][nx] == 0:
                            visited[ny][nx] = 1
                            q.append((ny, nx, chance, dist + 1))
        return -1

    input = stdin.readline
    n, m = map(int, input().split())
    _map = list(list(input().rstrip()) for _ in range(n))
    print(bfs())


if __name__ == "__main__":
    main()
