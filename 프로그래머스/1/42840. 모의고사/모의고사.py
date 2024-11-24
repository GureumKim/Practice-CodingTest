def solution(answers):
    def score_idiot1():
        score = 0
        for no in range(len(answers)):
            if no % 5 + 1 == answers[no]:
                score += 1
        return score
    def score_idiot2():
        score = 0
        even_pick = 2
        odd_pick = [1, 3, 4, 5]
        odd_idx = 0
        for no in range(0, len(answers), 2):
            if even_pick == answers[no]:
                score += 1
                
        for no in range(1, len(answers), 2):
            if odd_pick[odd_idx % 4] == answers[no]:
                score += 1
            odd_idx += 1
            
        return score
        
    def score_idiot3():
        score = 0
        pick = [3, 1, 2, 4, 5]
        even_idx, odd_idx = 0, 0
        for no in range(0, len(answers), 2):
            if pick[even_idx % 5] == answers[no]:
                score += 1
            even_idx += 1
        for no in range(1, len(answers), 2):
            if pick[odd_idx % 5] == answers[no]:
                score += 1
            odd_idx += 1
        
        return score
    
    
    answer = []
    scores = [0] * 4
    scores[1] = score_idiot1()
    scores[2] = score_idiot2()
    scores[3] = score_idiot3()
    
    mx = 0
    for st_no in range(1, 4):
        if mx == scores[st_no]:
            answer.append(st_no)
        elif mx < scores[st_no]:
            answer = []
            mx = scores[st_no]
            answer.append(st_no)
            
    
    return answer