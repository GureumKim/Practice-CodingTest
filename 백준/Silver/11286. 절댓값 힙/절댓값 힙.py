import sys;input = sys.stdin.readline
import heapq
h = []
for _ in range(int(input())):
    a = int(input())
    if a:
        heapq.heappush(h,(-a,-1)) if a<0 else heapq.heappush(h,(a,0))
    else:
        if h:
            num, sign = heapq.heappop(h)
            # num -> sign 순으로 작은 순서대로 나오게
            # 출력을 보니 음수부터 나옴
            print(-num if sign else num)
        else:
            print(a)