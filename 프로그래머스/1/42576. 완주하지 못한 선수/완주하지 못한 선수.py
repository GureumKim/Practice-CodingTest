def solution(participant, completion):

    hash = dict()
    for p in participant:
        hash[p] = hash.get(p, 0) + 1
    
    for c in completion:
        hash[c] -= 1
    
    for p in participant:
        if hash[p]:
            return p
    