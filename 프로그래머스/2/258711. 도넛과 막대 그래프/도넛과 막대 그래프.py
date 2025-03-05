def solution(edges):
    from collections import defaultdict
    edge_cnt = defaultdict(lambda: [0, 0])
    
    for s, e in edges:
        edge_cnt[s][0] += 1 #out
        edge_cnt[e][1] += 1 #in
    
    
    link_node = 0
    donut = bar = eight = 0
    for node in edge_cnt.keys():
        if edge_cnt[node][1] == 0 and edge_cnt[node][0] >= 2:
            link_node = node
            
        elif edge_cnt[node][0] == 0:
            bar += 1
        
        elif edge_cnt[node][0] == 2 and edge_cnt[node][1] >= 2: # link 노드로부터 시작되는 간선 유의
            eight += 1
    
    donut = edge_cnt[link_node][0] - eight - bar

    
    return [link_node, donut, bar, eight]