# n,k의 범위 -> 이게 좌표의 범위를 표현한 것이다.
# 테스트 케이스 범위가 클 때 연산을 줄인다, 괜히 조건 분기하지 않는다 + 숫자 많이 읽게 하지 않는다
from collections import deque

def bfs(start,end):
    global log
    q = deque()
    q.append((start,0))
    # 범위가 0부터고 이를 활용할 거니까 다른 수를 사용해서 방문 표시
    visited = [-1]*100001
    visited[start] = start

    if start > end:
        log = [x for x in range(end,start+1)]
        return start-end

    while q:
        now, cnt = q.popleft()
        if now == end:
            idx = now
            while idx != start:
                log.append(idx)
                idx=visited[idx]
            log.append(start)
            return cnt

        # direct 판별, 다음 갈 곳이 범위 내여야 가능
        if now*2<100001 and visited[2*now]==-1:
            q.append((2*now,cnt+1))
            visited[2*now] = now

        if now+1 < 100001 and visited[now+1]==-1:
            q.append((now+1,cnt+1))
            visited[now+1] = now

        if now-1>=0 and visited[now-1]==-1:
            q.append((now-1,cnt+1))
            visited[now-1] = now

log = []
print(bfs(*map(int,input().split())))
print(*log[::-1])