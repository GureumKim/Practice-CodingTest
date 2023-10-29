from sys import stdin; input= stdin.readline
import heapq
def dijkstra(s):
    heap = []
    heapq.heappush(heap,(0,s))
    result[s] = 0
    visited = [0]*(v+1)

    while heap:
        via_cost, via = heapq.heappop(heap)
        # via_cost 와 result[via]가 같을 때는 체크하지 않는다 (처음 자기 자신 방문 시에 바로 continue가 실행 됨)
        if visited[via] or via_cost > result[via]: continue
        # 자기 자신도 방문해야 하므로 visited 여부 체크 위치는 여기
        visited[via] = 1
        for next, cost in adj[via]:
            # print(next, cost)
            cost += via_cost
            if result[next] > cost:
                result[next] = cost
                heapq.heappush(heap,(cost,next))
            # print(result)

v, e = map(int,input().split())
start = int(input())
adj = [ [] for _ in range(v+1)]
for _ in range(e):
    fr, to, cost = map(int,input().split())
    adj[fr].append((to,cost))
    # 문제 조건 : 방향 그래프 -> 아래 코드 필요 x
    # adj[to].append((fr,cost))

inf = float("inf")
result = [inf]*(v+1)

dijkstra(start)

for i in range(1,v+1):
    print("INF" if result[i] == inf else result[i])