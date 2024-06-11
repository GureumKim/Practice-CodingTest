def solution(begin, target, words):
    from collections import deque

    wl = len(begin)
    words_count = len(words)
    q = deque()
    q.append((begin, 0)) # recent_word, start_idx, step
    used = [False]*words_count
    
    while q:
        recent_word, step = q.popleft()
        if recent_word == target:
            return step
        
        for i in range(words_count):
            if used[i]: continue
            cnt = 0
            for j in range(wl):
                if words[i][j] != recent_word[j]:
                    cnt += 1
                if cnt > 1: 
                    break
            if cnt == 1:
                used[i] = True
                q.append((words[i], step+1))
        # 나머지 경우는 자기 자신을 계속 추가해줄 필요가 없지                            
    return 0