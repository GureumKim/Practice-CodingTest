T = int(input())
decode = {
    "0001101": 0,
    "0011001": 1,
    "0010011": 2,
    "0111101": 3,
    "0100011": 4,
    "0110001": 5,
    "0101111": 6,
    "0111011": 7,
    "0110111": 8,
    "0001011": 9
}



for t in range(1, T + 1):
    answer = 0
    n, m = map(int, input().split())
    arr = list(input() for _ in range(n))

    encode = ""
    for i in range(n):
        for j in range(m - 1, 54, -1):
            if arr[i][j] == '1':
                encode = arr[i][j - 55 : j + 1] # 범위 조심!
                break

    # print(encode)

    code = [0]*8
    for i in range(8):
        code[i] = decode.get(encode[7 * i : 7 * i + 7])

    sum_odd, sum_even = 0, 0
    for i in range(8):
        if i % 2:
            sum_even += code[i]
        else:
            sum_odd += code[i]
    res = 3 * sum_odd + sum_even

    print(f"#{t} {0 if res % 10 else sum_odd + sum_even}")
