from sys import stdin
import heapq

input = stdin.readline


def dijkstra(s):
    h = []
    # *args, **kargs 이거 개념 다시
    heapq.heappush(h, (0, s))
    res[s] = 0
    visited = [0] * (n+1)

    while h:
        c, now = heapq.heappop(h)
        if visited[now] or res[now] < c: continue
        visited[now] = 1
        for nxt, cost in adj[now]:
            cost += c
            if cost <= res[nxt]:  # adj[s] 0이라서 '=' 필요
                res[nxt] = cost
                heapq.heappush(h, (cost, nxt))


n, m = int(input()), int(input())

adj = [[] for _ in range(n+1)]
INF = float('inf')
res = [INF] * (n+1)

for _ in range(m):
    s, e, v = map(int, input().split())
    adj[s].append((e, v))
start, end = map(int, input().split())

dijkstra(start)
# 출발점에서 도착점을 갈 수 있는 경우만 입력으로 주어진다.
print(res[end])
