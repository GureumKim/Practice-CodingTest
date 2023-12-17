from sys import stdin; input = stdin.readline

word1 = input().rstrip()
word2 = input().rstrip()

# word1_detail = [0]*26
# word2_detail = [0]*26

# for w in word1:
#     word1_detail[ord(w)-97] +=1
# for w in word2:
#     word2_detail[ord(w)-97] +=1

# cnt = 0
# for i in range(26):
#     cnt += abs(word1_detail[i] - word2_detail[i])
# print(cnt)

check = [0]*26

for w in word1:
    check[ord(w)-97] +=1
for w in word2:
    check[ord(w)-97] -=1

cnt2 = 0
for i in range(26):
    cnt2 += abs(check[i])
print(cnt2)