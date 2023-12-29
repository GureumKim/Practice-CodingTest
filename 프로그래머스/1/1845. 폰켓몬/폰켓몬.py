from math import ceil

def solution(nums):
    answer = 0
    
    hash = dict()
    
    for n in nums:
        if not hash.get(n):
            hash[n]=1

    if len(hash) >= ceil(len(nums)/2):
        answer = ceil(len(nums)/2)
    else:
        answer = len(hash)
    
    
    return answer

