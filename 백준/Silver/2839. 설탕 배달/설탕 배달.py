import sys;input=sys.stdin.readline
n = int(input())
s = 0
while n >= 0:
    if not n%5:
        s += n//5
        print(s)
        break
    n -= 3
    s += 1
else:
    print(-1)