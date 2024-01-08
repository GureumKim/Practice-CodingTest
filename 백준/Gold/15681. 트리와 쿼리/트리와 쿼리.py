from sys import stdin; input=stdin.readline #메모리 초과?
from sys import setrecursionlimit; setrecursionlimit(10**6)

# 메모이제이션 사용 -> dp..? 공부 필요

def make_tree(current_node,parent):
    for node in adj[current_node]:
        if node != parent:
            make_tree(node,current_node)

def count_subtree_nodes(current_node):
    size[current_node] = 1
    for node in adj[current_node]:
        if size[node]: continue
        count_subtree_nodes(node)
        size[current_node] += size[node]
    return size[current_node]

N,R,Q = map(int,input().split())
adj = [[] for _ in range(N+1)]
# children = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

size = [0]*(N+1)

# 왜 필요 없는 지 생각하기
# parent_ = [0]*(N+1)
# parent_[R] = -1

make_tree(R,-1)
count_subtree_nodes(R)

for _ in range(Q):
    print(size[int(input())])