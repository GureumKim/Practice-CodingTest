def solution(numbers, target):
    from functools import lru_cache

    @lru_cache(None)
    def dfs(l, t, last, v = 0):
        if l == last:
            return 1 if v == target else 0
        return dfs(l+1,t,last,v+numbers[l]) + dfs(l+1,t,last,v-numbers[l])

    return dfs(0,target,len(numbers))