a,b = input().split()
l_a, l_b = len(a), len(b)
a, b = int(a), int(b)
cnt = 0
def check(level=0,num=0):
    global cnt
    # print(num)
    if a <=int(num)<=b:
        cnt += 1

    if level == l_b:
        # print(cnt)
        return

    for n in [4, 7 ]:
        check(level+1,num*10+n)
        
check()
print(cnt)