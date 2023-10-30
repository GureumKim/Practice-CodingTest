import sys;input = sys.stdin.readline
n = int(input())
tri = [list(map(int,input().split())) for _ in range(n)]
for i in range(n-1):
    tri[i+1][0] += tri[i][0]
    tri[i+1][-1] += tri[i][-1]
for i in range(1,n-1):
    for j in range(1,i+1):
        tri[i+1][j] += max(tri[i][j-1], tri[i][j])
print(max(tri[-1]))