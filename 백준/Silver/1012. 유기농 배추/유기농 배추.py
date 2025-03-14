from sys import stdin, setrecursionlimit


def solution():
    input = stdin.readline
    setrecursionlimit(10**6)
    direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def dfs(y, x):
        for i, j in direct:
            dy, dx = y + i, x + j

            if dy < 0 or dy >= n or dx < 0 or dx >= m or visited[dy][dx] or not farm[dy][dx]: continue
            visited[dy][dx] = 1
            dfs(dy, dx)

    test_case = int(input())
    answer = []
    for _ in range(test_case):
        m, n, k = map(int, input().split())
        farm = [[0] * m for _ in range(n)]
        visited = [[0] * m for _ in range(n)]

        for _ in range(k):
            x, y = map(int, input().split())
            farm[y][x] = 1

        cnt_worm = 0
        for i in range(n):
            for j in range(m):
                if farm[i][j] == 1 and visited[i][j] == 0:
                    visited[i][j] = 1
                    cnt_worm += 1
                    dfs(i, j)

        answer.append(cnt_worm)

    print(*answer, sep="\n")


if __name__ == "__main__":
    solution()
