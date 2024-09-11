def main():
    from sys import stdin
    input = stdin.readline

    def dfs(start, level):
        if level == m:
            print(*sq)
            return

        prev = -1
        for i in range(start, n):
            if prev != num[i]:
                sq[level] = num[i]
                dfs(i + 1, level + 1)
                prev = num[i]

    n, m = map(int, input().split())
    num = sorted(map(int, input().split()))

    sq = [0] * m
    dfs(0, 0)


if __name__ == "__main__":
    main()
