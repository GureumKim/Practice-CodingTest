def main():
    from sys import stdin
    input = stdin.readline

    def dfs(start, level):
        if level == m:
            print(*sequence)
            return
        for i in range(start, n):
            sequence[level] = num[i]
            dfs(i + 1, level + 1)

    n, m = map(int, input().split())
    sequence = [0] * m
    num = list(map(int, input().split()))
    num.sort()

    dfs(0, 0)


if __name__ == "__main__":
    main()
