from bisect import *
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

lis = [arr[0]]

for i in range(1, n):
    if lis[-1] < arr[i]:
        lis.append(arr[i])
        continue

    pos = bisect_left(lis, arr[i])
    lis[pos] = arr[i]

print(len(lis))
