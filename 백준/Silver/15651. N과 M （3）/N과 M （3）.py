def main():
    from sys import stdin
    input = stdin.readline

    def dfs(level):
        if level == m:
            print(*sequence)
            return
        for i in range(1, n + 1):
            sequence[level] = i
            dfs(level + 1)

    n, m = map(int, input().split())
    sequence = [0] * m
    dfs(0)


if __name__ == "__main__":
    main()
