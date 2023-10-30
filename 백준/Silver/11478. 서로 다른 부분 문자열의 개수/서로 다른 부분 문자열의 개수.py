from sys import stdin; input= stdin.readline
S = input().rstrip()
hash = dict()

for l in range(1,len(S)+1):
    for s in range(0,len(S)):
        if not hash.get(S[s:s+l]):
            hash[S[s:s+l]] = 1
print(len(hash))