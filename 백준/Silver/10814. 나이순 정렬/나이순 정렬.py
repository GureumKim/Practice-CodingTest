import sys
input = sys.stdin.readline


# def get_list():
    # lst = []
    # for i in range(int(input())):
    #     age, name = input().split()
    #     lst.append((int(age), name, i))
    # return lst
def get_list():
    lst = [[] for _ in range(201)]
    for i in range(int(input())):
        age, name = input().split()
        lst[int(age)].append(name)
    return lst

# def sort_member(mem):
    # return sorted(mem, key=lambda x: (x[0], x[2]))


# def main():
#     members = get_list()
#     members = sort_member(members)
#     for m in members:
#         print(m[0], m[1])
def main():
    members = get_list()
    for i in range(201):
        if members[i]:
            for m in members[i]:
                print(i, m)
if __name__ == "__main__":
    main()
