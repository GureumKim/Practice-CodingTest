from sys import stdin

input = stdin.readline


def solution() -> None:
    def count(n: int) -> int:
        return n * (n - 1) // 2

    answer = 0
    n, m = map(int, input().split())
    num = list(map(int, input().split()))
    acc_sum = [0] * n
    cnt_remainder = [0] * m

    acc_sum[0] = num[0]
    for i in range(1, n):
        acc_sum[i] = num[i] + acc_sum[i - 1]
    for i in range(n):
        remainder = acc_sum[i] % m
        if remainder == 0:
            answer += 1
        cnt_remainder[remainder] += 1
    for i in range(m):
        answer += count(cnt_remainder[i])
    print(answer)


if __name__ == "__main__":
    solution()
