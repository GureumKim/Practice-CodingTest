n, k = map(int,input().split())
nums = list(map(int,input().split()))

start, end = 0, k
temp = sum(nums[start:end])
mx = temp

while end < n:
    temp = temp - nums[start] + nums[end]
    # print("start:", start, "end:",end)
    # print("mx:",mx, "temp:",temp)
    mx = max(temp,mx)
    start += 1
    end += 1
print(mx)