def main():
    from sys import stdin
    input = stdin.readline

    def dfs(level):
        if level == m:
            print(*sq)
            return

        for i in range(n):
            sq[level] = num[i]
            dfs(level + 1)

    n, m = map(int, input().split())
    num = sorted(map(int, input().split()))

    sq = [0] * m
    dfs(0)


if __name__ == "__main__":
    main()
