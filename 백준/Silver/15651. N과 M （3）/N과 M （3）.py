def dfs(n,m,level=0):
    # global cnt
    if level == m:
        print(*choice)
        # cnt+=1
        return
    for i in range(1,n+1):
        choice[level] = i
        dfs(n,m,level+1)

cnt = 0
n,m = map(int,input().split())
choice = [0]*m
dfs(n,m)
# print(cnt)