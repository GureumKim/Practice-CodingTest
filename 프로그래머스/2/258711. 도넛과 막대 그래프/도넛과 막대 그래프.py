def solution(edges):
    
    answer = []
    num_of_edges = len(edges)
    # node의 자신을 향하는 간선과 다른 노드를 향하는 간선의 수를 저장
    # [들어오는 간선의 수, 나가는 간선의 수]
    node_info = [[0,0,[],False] for _ in range(10**6+1)]
    
    for i in range(num_of_edges):
        from_, to_ = edges[i][0], edges[i][1]
        node_info[from_][1] += 1
        node_info[to_][0] += 1
        node_info[from_][2].append(to_)
        node_info[from_][3], node_info[to_][3] = True, True
            
    cnt_bar, cnt_eight, cnt_donut = 0, 0, 0
    
    # 막대랑 8자 둘 다 없으면 0이어야 함, 0으로 초기화
    added_node, graph_connected = 0, 0
    for i in range(1,10**6+1):
        if node_info[i][0] == 0 and node_info[i][1] >= 2:
            added_node = i
            graph_connected = node_info[i][1]
            for n in range(node_info[i][1]):
                node_info[node_info[i][2][n]][0] -= 1
            break
              
    for i in range(1,10**6+1):
        if node_info[i][3] != True:
            continue
        if node_info[i][0] == 2 and node_info[i][1]== 2:
            cnt_eight += 1
        elif node_info[i][0] == 0 and i != added_node:
            cnt_bar += 1
            
    cnt_donut = node_info[added_node][1] - cnt_eight - cnt_bar       
    
    answer = [added_node, cnt_donut, cnt_bar, cnt_eight]
    
    return answer