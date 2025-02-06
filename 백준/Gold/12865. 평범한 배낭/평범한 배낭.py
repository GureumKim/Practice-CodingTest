import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]

data = []
for _ in range(n):
    data.append(map(int, input().split()))
    
for i in range(1, n + 1):
    w, v = data[i - 1]
    for j in range(1, k + 1):
        if w > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], v + dp[i - 1][j - w])
print(dp[n][k])
