def main():
    from sys import stdin
    input = stdin.readline

    def dfs(level):
        if level == m:
            print(*sequence)
            return
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                sequence[level] = num[i]
                dfs(level + 1)
                visited[i] = False

    n, m = map(int, input().split())
    sequence = [0] * m
    visited = [False] * n
    num = list(map(int, input().split()))
    num.sort()

    dfs(0)


if __name__ == "__main__":
    main()
