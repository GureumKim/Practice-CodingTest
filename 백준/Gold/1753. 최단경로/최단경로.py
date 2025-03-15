from sys import stdin
import heapq as hq


def dijkstra(start):
    visited = [0] * (V + 1)
    heap = []
    hq.heappush(heap, (0, start))  # 자기 자신(start)도 경유하기 때문에 visited 체크 x
    res[start] = 0

    while heap:
        v_cost, via = hq.heappop(heap)
        if visited[via]: continue
        visited[via] = 1

        if res[via] < v_cost: continue
        for nxt, c in adj[via]:
            cost = c + v_cost
            if res[nxt] > cost:
                res[nxt] = cost
                hq.heappush(heap, [res[nxt], nxt])


input = stdin.readline

V, E = map(int, input().split())
K = int(input())

adj = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append([v, w])

INF = float('inf')
res = [INF] * (V + 1)

dijkstra(K)

answer = []
for i in range(1, V + 1):
    if res[i] == INF:
        answer.append("INF")
    else:
        answer.append(f"{res[i]}")

print(*answer, sep="\n")
