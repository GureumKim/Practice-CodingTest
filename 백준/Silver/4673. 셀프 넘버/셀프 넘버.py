sieve = [0] * 10001

for i in range(1,10001):
    if sieve[i] : continue
    next = i
    while 1:
        now = next
        while 1:
            now, mod = divmod(now,10)
            next += mod
            if now == 0: break
        if next > 10000: break
        sieve[next] = 1

for i in range(1,10001):
    if not sieve[i]:
        print(i)