def main():
    from sys import stdin
    input = stdin.readline

    def dfs(now, level):
        if level == m:
            print(*sequence)
            return
        for i in range(now, n + 1):
            sequence[level] = i
            dfs(i, level + 1)
    n, m = map(int, input().split())
    sequence = [0] * m
    dfs(1, 0)


if __name__ == "__main__":
    main()
