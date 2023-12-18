import sys; input = sys.stdin.readline

def divide_and_conquer(base,exponential):
  if exponential == 1:
    return base
  elif exponential%2:
    res = divide_and_conquer(base,exponential//2)
    return res*res*base%1000000007
  else:
    res = divide_and_conquer(base,exponential/2)
    return res*res%1000000007
    
k, p, n = map(int,input().split())
ans = k*divide_and_conquer(p,10*n)%1000000007
print(ans)