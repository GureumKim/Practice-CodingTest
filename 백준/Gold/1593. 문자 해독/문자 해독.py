import sys; input = sys.stdin.readline

g, s = map(int, input().split())
W = input().rstrip()
S = input().rstrip()

w_check = [0] * 128
s_check = [0] * 128

for w in W:
    w_check[ord(w)] += 1

start, length = 0, 0
cnt = 0

for i in range(s):
    s_check[ord(S[i])] += 1
    length += 1

    if length == g:
        if w_check == s_check:
            cnt += 1
        s_check[ord(S[start])] -= 1
        start += 1
        length -= 1
print(cnt)