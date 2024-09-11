def main():
    from sys import stdin
    input = stdin.readline

    def dfs(level):
        if level == m:
            print(*sequence)
            return
        for i in range(1, n + 1):
            if not visited[i - 1]:
                sequence[level] = i
                visited[i - 1] = True
                dfs(level + 1)
                visited[i - 1] = False

    n, m = map(int, input().split())
    sequence = [0] * m
    visited = [False] * n
    dfs(0)


if __name__ == "__main__":
    main()
