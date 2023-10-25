from sys import stdin; input = stdin.readline
def cycle(now,visited):
    if not visited[choices[now]]:
        visited[choices[now]] = 1
        cycle(choices[now],visited)
    return 1

def dfs(level=0):
    global mx,mn
    if level == n:
        group = 0
        visited = [0]*n
        res = 1
        for i in range(n):
            res *= scores.get(dominos[i][choices[i]])
        for i in range(n):
            if not visited[i]:
                group += cycle(i,visited)
        if group%2 == 0:
            res *= -1
        mx,mn = max(mx,res), min(mn,res)
        return

    for i in range(n):
        if used[i]: continue
        used[i] = 1
        choices[level] = i
        dfs(level+1)
        used[i] = 0

n = int(input())
dominos = [list(input()) for _ in range(n)]    # 1 ~ 6

scores = dict()
for i in range(10):
    scores[str(i)] = i
for i in range(1,10):
    scores[chr(i+64)] = -i

choices = [0]*n
used = [0]*n
mn, mx = float('inf'), -float('inf')
dfs()
print(f"{mn}\n{mx}")