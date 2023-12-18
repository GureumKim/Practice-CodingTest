from sys import stdin; input = stdin.readline

n, k = map(int,input().split()) # n: 물품 수, k: 버틸 수 있는 무게
dp = [[0]*(k+1) for _ in range(n+1)]

things = []
for _ in range(n):
    things.append(tuple(map(int,input().split())))

# 그리디는 최적 해가 되지 못한다
# things = sorted(things,key = lambda  x: x[0])
# print(things)

for i in range(1,n+1):
    for j in range(1, k+1):
        w = things[i-1][0]
        v = things[i-1][1]

        if j <w: # 가방에 넣을 수 없다면
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],v+dp[i-1][j-w])
print(dp[n][k])