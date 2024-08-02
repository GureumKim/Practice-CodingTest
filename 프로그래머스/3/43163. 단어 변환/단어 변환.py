# 최소 단계 찾는 거니까 => BFS가 더 적합!!!

def solution(begin, target, words):
    from collections import deque
    
    def can_transform(w1, w2):
        if w1 == w2: 
            return -1
        
        cnt =  0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                cnt += 1
                if cnt > 1:
                    return False
        return True
    
    step = 0
    q = deque([(begin, 0)])    
    # q.append((begin, 0))
    
    used = [False] * len(words)
    
    while q:
        word, step = q.popleft()
        if word == target: # begin 과 target은 같지 않음
            return step
        
        for i in range(len(words)):
            if used[i] : continue
            
            if can_transform(word, words[i]):
                used[i] = True
                q.append((words[i], step + 1))
    return 0
                