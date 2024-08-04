from sys import stdin
import heapq
inp = stdin.readline

heap = []

for _ in range(int(inp())):
    heapq.heappush(heap, int(inp()))

cnt = 0
while True:
    a = heapq.heappop(heap)
    if heap:
        b = heapq.heappop(heap)
        cnt += a+b
        heapq.heappush(heap, a+b)
    else:
        break
print(cnt)