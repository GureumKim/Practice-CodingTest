star = ["***","* *","***"]
n = int(input())

# 3**1 ~ 3**K까지
# star은 이미 K=1일 때
# k = K-1, 이때 까지 재귀한다
k = 0
while n !=3:
    n //= 3
    k += 1

def mkstar(star,l):
    temp = []
    for i in range(3*l):
        if i // l == 1:
            temp.append(star[i%l]+" "*l+star[i%l])
        else:
            temp.append(star[i%l]*3)
    return temp

for i in range(1,k+1):
    star = mkstar(star, 3**i)

for s in star:
    print(s)