def solution(s):
    def calc_len():
        pass
    
    def split():
        pass

    
    l = len(s)
    min_ = l
    
    for i in range(1, l):
        start, end = 0, i
        temp = "" 
        now = s[start:start + i]
        cnt = 1
        while 1:
            next = s[end: end + i]
            if now == next:
                cnt+=1
            else:
                if cnt == 1:
                    temp += now
                else:
                    temp += f"{cnt}{now}"
                now = s[end: end + i]
                cnt = 1
            # print(temp)
            start += i
            if end + i > l:
                if cnt > 1:
                    temp += f"{cnt}{s[end:]}"
                else:
                    temp += f"{s[end:]}"
                # print(temp)
                break
            end += i
        min_ = min(len(temp), min_)
        # print("min:", min_)
    
    return min_
