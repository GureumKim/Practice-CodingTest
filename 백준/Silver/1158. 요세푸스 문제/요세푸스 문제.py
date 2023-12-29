n, K = map(int,input().split())
nums = list(range(1,n+1))
ans = []

k = K - 1
for i in range(len(nums)):
    if len(nums)>k:
        ans.append(nums.pop(k))
        k += K - 1
    elif len(nums) <= k:
        k %= len(nums)
        ans.append(nums.pop(k))
        k += K - 1

print("<",end='')
print(*ans,sep=', ',end='')
print(">")