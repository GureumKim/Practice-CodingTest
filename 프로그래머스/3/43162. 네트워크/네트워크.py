def solution(n, computers):
    checked = [False] * n
    answer = 0
    
    def dfs(now):
        checked[now] = True
        for i in range(n):
            if not checked[i] and computers[now][i] == 1:
                dfs(i)
        
    for i in range(n):
        if not checked[i]:
            dfs(i)
            answer += 1
    
    return answer