def main():
    from sys import stdin
    input = stdin.readline

    def dfs(level):
        if level == m:
            print(*sq)
            return

        prev = -1
        for i in range(n):
            if prev != num[i] and not visited[i]:
                visited[i] = True
                sq[level] = num[i]
                dfs(level + 1)
                visited[i] = False
                prev = num[i]

    n, m = map(int, input().split())
    sq = [0] * m
    visited = [False] * n

    num = sorted(map(int, input().split()))
    dfs(0)


if __name__ == "__main__":
    main()
