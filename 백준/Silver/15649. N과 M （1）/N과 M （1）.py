def dfs(n,m,level=0):
    if level == m:
        print(*choice)
        return
    for i in range(1,n+1):
        if not used[i]:
            used[i] = 1
            choice[level] = i
            dfs(n,m,level+1)
            used[i] = 0

n,m = map(int,input().split())
choice = [0]*m
used = [0]*(n+1)
dfs(n,m)