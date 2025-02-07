import sys
input = sys.stdin.readline

n = int(input())

score = [0] * n
A = [0] * n # 이전꺼 밟지 않고
B = [0] * n # 이전꺼 밟고
for i in range(n):
    score[i] = int(input())

A[0] = B[0] = score[0]

for i in range(1, n):
    if i >= 2:
        A[i] = score[i] + max(A[i - 2], B[i - 2])
    else:
        A[i] = score[i]

    if i >= 3:
        B[i] = score[i] + score[i - 1] + max(A[i - 3], B[i - 3])
    else:
        B[i] = score[i] + score[i - 1]

print(max(A[n - 1], B[n - 1]))
