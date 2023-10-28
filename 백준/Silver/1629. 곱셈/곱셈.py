# review 노트 작성하기
a, b, c = map(int,input().split())
def pow(A,expo):
    if expo == 1:
        return A % c

    temp = pow(A,expo//2)

    if expo %2 == 1:
        return (temp*temp%c) * A %c
    return temp * temp % c
print(pow(a,b))