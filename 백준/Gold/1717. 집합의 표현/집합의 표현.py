import sys
#sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 늘리기
inp = sys.stdin.readline

n, m = map(int, inp().split())
parents = list(range(n+1))

def find_root(cur):
    if parents[cur] != cur:
        parents[cur] = find_root(parents[cur])  # 경로 압축
    return parents[cur]

def union(a, b):
    ra, rb = find_root(a), find_root(b)
    if ra != rb:
        parents[rb] = ra  # 부모를 합침 (간단하게 rb의 부모를 ra로 설정)

for _ in range(m):
    command, n1, n2 = map(int, inp().split())
    if command == 1:
        if find_root(n1) == find_root(n2):
            print("YES")
        else:
            print("NO")
    else:
        union(n1, n2)