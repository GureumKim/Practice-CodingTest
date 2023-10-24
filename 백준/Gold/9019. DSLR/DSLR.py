from sys import stdin;

input = stdin.readline
from collections import deque

def bfs(start, end):
    q = deque()
    q.append((start, ""))

    visited = [0] * 10001
    visited[start] = 1
    while q:
        now, ans = q.popleft()

        if now == end:
            return ans

        d = now * 2 % 10000
        if not visited[d]:
            visited[d] = 1
            q.append((d, ans + 'D'))

        s = (now - 1) % 10000
        if not visited[s]:
            visited[s] = 1
            q.append((s, ans + 'S'))

        a, b = divmod(now, 1000)
        l = b * 10 + a
        if not visited[l]:
            visited[l] = 1
            q.append((l, ans + 'L'))

        a, b = divmod(now, 10)
        r = b * 1000 + a
        if not visited[r]:
            visited[r] = 1
            q.append((r, ans + 'R'))

for _ in range(int(input())):
    value, result = map(int, input().split())
    ans = bfs(value, result)
    print(ans)