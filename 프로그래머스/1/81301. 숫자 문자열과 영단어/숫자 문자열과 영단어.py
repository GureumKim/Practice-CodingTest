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
                # 여기 처음에는 answer = table.get(word) 였는데 맞았다고 뜸...
                answer += table.get(word)
                word = ''
            answer += s
        else:
            word += s
    
        # 키 확인은 word in table 이렇게 하면 해시 조회해서 다 빠르다고 함..
        if word in table.keys():
            answer += table.get(word)
            word = ''
               
    answer = int(answer)
    
    return answer