def solution(n, computers):
    answer = 0
    visited = [False] * n 
    
    def dfs(start):
        visited[start] = True
        
        for i in range(n):
            # 실수한 점-> 무엇을 비교하는지 (visited의 인덱스가 무엇이 되어야 하는 지 정확히 파악하기)
            if computers[start][i] and not visited[i]:
                dfs(i)
    
    for i in range(n):
        if visited[i]:
            continue
        dfs(i)
        answer += 1
    
    return answer
