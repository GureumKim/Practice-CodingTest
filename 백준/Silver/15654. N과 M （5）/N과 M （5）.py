from itertools import permutations as pm
n,m = map(int,input().split())
lst = list(input().split())
print('\n'.join(map(' '.join,pm(sorted(lst,key=lambda x:(len(x),x)),m))))