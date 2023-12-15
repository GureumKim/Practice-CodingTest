from sys import stdin; input = stdin.readline
n, m = map(int,input().split())

nums = [[0]*(n+1)] + [[0]+list(map(int,input().split())) for _ in range(n)]
# print(nums)
for i in range(1,n+1):
    for j in range(1,n+1):
        nums[i][j] += nums[i-1][j]+nums[i][j-1]-nums[i-1][j-1]

# print(nums)
for k in range(m):
    x1, y1, x2, y2 = map(int,input().split())
    # print(x1,y1,x2,y2)
    ans = nums[x2][y2] - nums[x1-1][y2] - nums[x2][y1-1] + nums[x1-1][y1-1]
    print(ans)