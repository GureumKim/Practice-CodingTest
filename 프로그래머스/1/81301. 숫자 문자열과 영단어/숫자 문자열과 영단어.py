def solution(S):
    table = {
        'zero' : '0',
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9'
    }
    
    answer = ''
    word = ''
    for s in S:
        if s in table.values():
            if word:
                answer = table.get(word)
                word = ''
            answer += s
        else:
            word += s
    
        if word in table.keys():
            answer += table.get(word)
            word = ''
               
    answer = int(answer)
    
    return answer