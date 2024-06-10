def solution(numbers, target):
    from functools import lru_cache
    
    # least recent used cache 
    # @lru_cache(maxsize)
    @lru_cache(None)
    def dfs(lev = 0, value = 0):
        if lev == len(numbers):
            return 1 if value == target else 0
        
        return dfs(lev + 1, value + numbers[lev]) + dfs(lev + 1, value - numbers[lev])
    
    return dfs()