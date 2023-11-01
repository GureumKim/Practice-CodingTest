## MUST REVIEW 
## 1부터 끝 범위까지 & i를 나누는 수로 생각
## 몫, 나머지 개념 및 특징 활용
n = int(input())

dp = [0] * (n + 1)

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[n])