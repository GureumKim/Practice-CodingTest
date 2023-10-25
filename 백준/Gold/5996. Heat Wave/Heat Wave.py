from sys import stdin; input=stdin.readline
import heapq

def dijkstra(start):
    visited = [0]*(T+1)
    heap = []
    heapq.heappush(heap,(0,start))  #
    result[start] = 0

    while heap:
        v_cost, via = heapq.heappop(heap)
        if visited[via]: continue
        visited[via] = 1
        if result[via] < v_cost: continue
        for next, c in adj[via]:
            cost = v_cost+c
            if result[next] > cost:
               result[next] = cost
               heapq.heappush(heap,(result[next],next))

T, C, Ts, Te = map(int,input().split()) # Ts -> Te print(minimum cost)
adj = [[] for _ in range(T+1)]
for _ in range(C):
    r1, r2, cost = map(int,input().split())
    adj[r1].append((r2,cost))
    adj[r2].append((r1,cost))

result = [float('inf')]*(T+1)
dijkstra(Ts)
print(result[Te])