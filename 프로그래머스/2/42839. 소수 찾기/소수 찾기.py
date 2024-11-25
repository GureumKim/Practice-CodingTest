from itertools import permutations
def mk_seive(n):
    seive = [True for _ in range(n + 1)]
    seive[0], seive[1] = False, False
    
    for i in range(2, int(n ** 0.5) + 1):
        for j in range(2 * i, n + 1, i):
            seive[j] = False
    
    return seive


def solution(numbers):
    answer = 0
    seive = mk_seive(10**7)
    
    candidates = set()
    for n in range(1, len(numbers) + 1):
        p = permutations(numbers, n)
        for v in p:
            k = int(''.join(list(v)))
            candidates.add(k)
    print(candidates)
    for n in list(candidates):
        if seive[n]:
            print(seive[n])
            answer += 1
    return answer