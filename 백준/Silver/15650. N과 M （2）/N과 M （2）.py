def dfs(n,m,level=0,start=1):
    if level == m:
        print(*choice)
        return
    for i in range(start,n+1):
        choice[level] = i
        dfs(n,m,level+1,i+1)


n,m = map(int,input().split())
choice = [0]*m
dfs(n,m)