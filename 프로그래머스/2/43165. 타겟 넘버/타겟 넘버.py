def solution(numbers, target):
    answer = 0 
    
    level = len(numbers)
    now = 0
    
    def dfs(value, lev = 0):
        ans = 0
        if lev == level:
            if value == target:
                # answer += 1
                return 1
            return 0
        
        ans += dfs(value + numbers[lev], lev+1)
        ans += dfs(value - numbers[lev], lev + 1)
        return ans
    
    answer = dfs(now)
    return answer