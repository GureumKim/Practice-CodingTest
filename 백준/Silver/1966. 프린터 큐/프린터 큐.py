for _ in range(int(input())):
    n, m = map(int,input().split())
    priorities = list(map(int,input().split()))

    q = []
    for i in range(n):
        q.append((priorities[i],i))

    priorities = sorted(priorities,key=lambda x:x,reverse=True)
    # print(q)
    # print(priorities)
    idx = 0
    cnt = 1
    while 1:
        if q[idx][0] == priorities[0]:
            if q[idx][1] == m:
                print(cnt)
                break
            # 출력 후 cnt 증가
            else:
                priorities.pop(0)
                cnt += 1

        idx = (idx+1)%n