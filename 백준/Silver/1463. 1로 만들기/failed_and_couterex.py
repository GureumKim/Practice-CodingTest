# 얘는 왜 틀림...?
# 반례
"""
321은 정답이 9이고, 214는 정답이 10입니다. 이는 321을 1로 만드는 가장 짧은 과정이 321을 3으로 나누는 것이 아닌 1을 빼는 것으로 시작하기 때문입니다.

따라서 642는 실제로 2로 먼저 나누는 것이 정답인데, 3으로 나누는 경우만 확인하게 되어 오답이 나오게 됩니다.

642: 10
642 321 320 160 80 40 20 10 9 3 1

321: 9
321 320 160 80 40 20 10 9 3 1

214: 10
214 107 106 53 52 26 13 12 4 2 1
"""

from copy import deepcopy
n = int(input())

if n == 1:
    print(0)
else:
    dp = [n]*3
    cnt = 0
    while 1:
        temp = deepcopy(dp)
        for i in range(3):
            a,b = divmod(temp[i],3)
            if b==0 and dp[0] > a:
                dp[0] =a

            # 여기서도 처음에 else를 사용했는데
            # 2로 나누고 1빼고 다음 과정으로 넘어가는게 제일 빠를 수 있는 반례를 놓침
            a,b = divmod(temp[i],2)
            if b == 0 and dp[1] >a:
                dp[1] = a
            # if dp[2] > temp[i] -1:
            #     dp[2] = temp[i] - 1
            dp[2] = min(temp[i]-1,dp[2])
        cnt+=1
        print(dp)
        if dp.count(1): break
    print(cnt)
