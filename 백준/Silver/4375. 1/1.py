import sys
input = sys.stdin.readline
def m(n):
    i=1
    N=1
    while N%n !=0:
        N=N*10+1
        i+=1
    print(i)


if __name__ == "__main__":
    while True:
        try:
            n=int(input())
            m(n)
        except:
            break