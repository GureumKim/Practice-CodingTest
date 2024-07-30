import sys
input_ = sys.stdin.readline


class Main:
    def __init__(self):
        self.nums = []
        self.n, self.k = int(input_()), int(input_())
        self.visited = [False] * self.n
        self.res = set()

    def check_combination(self):
        self.dfs()

    def do(self):
        for _ in range(self.n):
            self.nums.append(input_().rstrip())
        self.check_combination()
        print(len(self.res))
        # print(self.res)

    def dfs(self, level=0, temp=""):
        if level == self.k:
            self.res.add(temp)
            # print("level :", level, "temp: ", temp)
            return
        for i in range(self.n):
            if self.visited[i]:
                continue
            self.visited[i] = True
            self.dfs(level+1, temp+self.nums[i])
            self.visited[i] = False


main = Main()
main.do()
