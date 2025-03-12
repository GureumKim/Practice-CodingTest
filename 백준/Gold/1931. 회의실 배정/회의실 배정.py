from sys import stdin
import heapq as hq

input = stdin.readline

heap = []

for _ in range(int(input())):
    s, e = map(int, input().split())
    hq.heappush(heap, (e, s))

answer = 0
from_available = 0
while heap:
    e, s = hq.heappop(heap)
    if s >= from_available:
        answer += 1
        from_available = e

print(answer)
