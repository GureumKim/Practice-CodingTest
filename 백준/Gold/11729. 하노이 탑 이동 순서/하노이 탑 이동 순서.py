# 하노이 => An+1 = 2An + 1 <=> An = 2**n - 1
res = []
cnt = 0
def hanoi(n,start,end,mid):
    global cnt
    if n == 1:
        res.append([start,end])
        cnt += 1
        return
    hanoi(n-1,start,mid,end)
    res.append([start,end])
    cnt += 1
    hanoi(n-1,mid,end,start)
hanoi(int(input()),1,3,2)
print(cnt)
for frm, to in res:
    print(frm, to)

# 참고. https://velog.io/@jewon119/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B8%B0%EC%B4%88-%ED%95%98%EB%85%B8%EC%9D%B4%EC%9D%98-%ED%83%91Tower-of-Hanoi