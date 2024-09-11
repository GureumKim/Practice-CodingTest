def main():
    from sys import stdin
    input = stdin.readline

    def dfs(level):
        if level == m:
            print(*sq)
            return

        for idx in range(len(num)):
            if num_cnt[num[idx]] > 0:
                sq[level] = num[idx]
                num_cnt[num[idx]] -= 1
                dfs(level + 1)
                num_cnt[num[idx]] += 1

    n, m = map(int, input().split())
    sq = [0] * m
    num_cnt = [0] * (10 ** 4 + 1)

    lst = list(map(int, input().split()))
    num = list()
    for i in range(n):
        if num_cnt[lst[i]] == 0:
            num.append(lst[i])
        num_cnt[lst[i]] += 1
    num.sort()

    dfs(0)


if __name__ == "__main__":
    main()
