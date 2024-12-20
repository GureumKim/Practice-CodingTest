from sys import stdin

input = stdin.readline

def solution():
    answer = []

    is_submit = [False] * 31
    for _ in range(28):
        no = int(input())
        is_submit[no] = True
    for i in range(1, 31):
        if not is_submit[i]:
            answer.append(str(i))
    print("\n".join(answer))


if __name__ == "__main__":
    solution()
