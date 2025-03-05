def solution(edges):
    from collections import defaultdict
    edge_cnt = defaultdict(lambda: [0, 0])
    
    for s, e in edges:
        edge_cnt[s][0] += 1
        edge_cnt[e][1] += 1
    
    return 