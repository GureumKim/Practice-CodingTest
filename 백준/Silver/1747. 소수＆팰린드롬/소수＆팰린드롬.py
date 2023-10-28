n = int(input())

aristo = [True]*(1000000)
aristo[1] = 0

for i in range(2,int(1000000**0.5)+1):
    for j in range(2*i,1000000,i):
        if aristo[j]:
            aristo[j] = False
# 98689까지가 100만 이하 중에 최대
for i in range(n,98690):
    if aristo[i] and str(i) == str(i)[::-1]:
        print(i)
        break
else:
    print(1003001)
    
# for i in range(999999,-1,-1):
#     if aristo[i] and str(i) == str(i)[::-1]:
#         print(i)
#         break