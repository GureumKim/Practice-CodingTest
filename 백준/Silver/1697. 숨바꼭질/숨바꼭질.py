from collections import deque
n, k = map(int,input().split())

q = deque()
q.append((n,0))
visited = [0]*100001
visited[n] = 1

while q:
    now, time = q.popleft()
    if now == k:
        print(time)
        break
    if now - 1 >=0 and not visited[now-1]:
        visited[now-1] = 1
        q.append((now-1,time+1))
    if now + 1 <= 100000 and not visited[now+1]:
        visited[now+1] = 1
        q.append((now+1,time+1))
    if 2*now <= 100000 and not visited[2*now]:
        visited[2*now] = 1
        q.append((2*now,time+1))