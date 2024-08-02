# 최소 단계 찾는 거니까 => BFS가 더 적합!!!

def solution(begin, target, words):
    from collections import deque
    
    def compare(w1, w2):
        if w1 == w2: 
            return -1
        
        cnt, idx = 0, 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                cnt += 1
                if cnt > 1:
                    return -1
                idx = i
        return idx
    
    step = 0
    q = deque()    
    q.append((begin, 0))
    
    used = [False] * len(words)
    
    while q:
        word, step = q.popleft()
        if word == target: # begin 과 target은 같지 않음
            return step
        
        for i in range(len(words)):
            if used[i] : continue
            res = compare(word, words[i])
            if res != -1:
                used[i] = True
                q.append((word[:res] + words[i][res] + word[res+1:], step + 1))
    return 0










# def solution(begin, target, words):
#     from collections import deque

#     wl = len(begin)
#     words_count = len(words)
#     q = deque()
#     q.append((begin, 0)) # recent_word, start_idx, step
#     used = [False]*words_count
    
#     while q:
#         recent_word, step = q.popleft()
#         if recent_word == target:
#             return step
        
#         for i in range(words_count):
#             if used[i]: continue
#             cnt = 0
#             for j in range(wl):
#                 if words[i][j] != recent_word[j]:
#                     cnt += 1
#                 if cnt > 1: 
#                     break
#             if cnt == 1:
#                 used[i] = True
#                 q.append((words[i], step+1))
#         # 나머지 경우는 자기 자신을 계속 추가해줄 필요가 없지                            
#     return 0