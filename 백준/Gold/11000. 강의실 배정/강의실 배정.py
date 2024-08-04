from sys import stdin
import heapq
inp = stdin.readline

def solution(lectures):
    lectures = sorted(lectures)
    min_heap = []
    for Sti, Eti in lectures:
        if min_heap and min_heap[0] <= Sti:
            heapq.heappop(min_heap)
        heapq.heappush(min_heap, Eti)
    return len(min_heap)

lectures = []
n = int(inp())
for _ in range(n):
    s, e = map(int, inp().split())
    lectures.append((s, e))

print(solution(lectures))