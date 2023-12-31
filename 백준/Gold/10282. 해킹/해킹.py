import heapq
import sys; input = sys.stdin.readline

def dijkstra(c,res,adj,v):
    heap = []
    heapq.heappush(heap,(0,c))


    while heap:
        via_cost, now = heapq.heappop(heap)
        if via_cost > res[now]: continue

        if v[now] : continue
        v[now] = 1

        for next, cost in adj[now]:
            # print(next)
            cost += via_cost
            # print(res[next], " : " , cost)
            # print(visited)
            if res[next] > cost:
                res[next] = cost
                heapq.heappush(heap,(cost,next))

    max_ = 0
    infected = 0
    for t in res:
        if t < inf:
            infected += 1
            max_ = max(max_,t)
    # print(now)
    return infected, max_


inf = float('inf')

for _ in range(int(input())):
    n, d, c= map(int,input().split())

    adj_arr = [[] for _ in range(n+1)]

    for _ in range(d):
        a,b, s = map(int,input().split())
        # print(a)
        # print(b)
        adj_arr[b].append((a,s))
    # print(adj)

    result = [inf]*(n+1)
    visited = [0]*(n+1)
    result[c] = 0
    # visited[c] = 1
    print(*dijkstra(c,result,adj_arr, visited))