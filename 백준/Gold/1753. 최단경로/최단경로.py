import heapq

def dijkstra(start):
    visited = [0]*(V+1)
    heap = []
    heapq.heappush(heap,(0,start))
    # 자기 자신도 경유할 거기 때문에 미리 visited에 체크하지 않음!
    # visited[start]=1
    res[start] = 0

    while heap:
        v_cost, via = heapq.heappop(heap)
        if visited[via]: continue
        visited[via] = 1

        if res[via] < v_cost: continue
        for next, c in adj[via]:
            cost = c+ v_cost
            if res[next] > cost:
                res[next] = cost
                heapq.heappush(heap,(res[next],next))

V, E = map(int,input().split())
adj = [[] for _ in range(V+1)]
start = int(input())
for _ in range(E):
    u,v,w = map(int,input().split())
    adj[u].append((v,w))

INF = float('inf')
res = [INF]*(V+1)
dijkstra(start)
for i in range(1,V+1):
    print("INF" if res[i]==INF else res[i])