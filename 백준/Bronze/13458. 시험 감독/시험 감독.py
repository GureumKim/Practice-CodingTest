from sys import stdin; input = stdin.readline
from math import ceil

n = int(input())
numbs = list(map(int,input().split()))
b, c = map(int, input().split())

ans = 0
for numb in numbs:
    if numb <= b:
        ans += 1
    else:
        ans += 1 + ceil((numb - b) / c)

print(ans)