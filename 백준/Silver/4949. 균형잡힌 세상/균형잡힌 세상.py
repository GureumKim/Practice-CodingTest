from sys import stdin
input = stdin.readline


def solution():
    def check(line):
        stack = []
        dic = {
            "(": -1,
            ")": 1,
            "[": -2,
            "]": 2
        }
        for l in line:
            if l in ["(", "["]:
                stack.append(l)
            elif l in [")", "]"]:
                if not stack:
                    print("no")
                    return
                prev = stack.pop()
                if dic[prev] + dic[l] != 0:
                    print("no")
                    return
        print("yes") if not stack else print("no")
    while True:
        l = input().rstrip()
        if l[0] == ".":
            return
        check(l)


if __name__ == "__main__":
    solution()
