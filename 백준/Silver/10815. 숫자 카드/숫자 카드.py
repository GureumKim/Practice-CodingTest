from sys import stdin
input = stdin.readline

def solution():
    n = int(input())
    card = list(map(int, input().split()))
    m = int(input())
    comp = list(map(int, input().split()))

    status_isExist = [False] * (2 * 10 ** 7 + 1)
    ans = []

    for c in card:
        status_isExist[c + 10**7] = True
        
    for c in comp:
        if status_isExist[c + 10**7]:
            ans.append(1)
        else:
            ans.append(0)
    print(*ans)

if __name__ == "__main__":
    solution()