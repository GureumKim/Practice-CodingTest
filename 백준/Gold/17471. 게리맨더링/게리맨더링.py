def main():
    from sys import stdin
    from itertools import combinations
    from collections import deque, defaultdict

    input = stdin.readline

    def get_population(group):
        res = 0
        for i in group:
            res += population[i]
        return res

    def check(group):
        if len(group) == 1:
            return True
        q = deque()
        q.append(group[0])
        visited = [0] * (n + 1)

        while q:
            now = q.popleft()
            for adj_node in adj[now]:
                if visited[adj_node] == 0 and adj_node in group:
                    visited[adj_node] = 1
                    q.append(adj_node)
        for d in group:
            if visited[d] == 0:
                return False
        return True

    # 입력 받기
    n = int(input())
    population = [0] + list(map(int, input().split()))

    adj = [[]] # 인접 리스트
    for i in range(n):
        num, *neighbor = map(int, input().split())
        adj.append(neighbor)

    # district = set(range(n))
    district = list(range(1, n + 1))
    mn = float('inf')
    for i in range(1, n):
        for group1 in combinations(district, i // 2 + 1): # 선거구 조합 만들기, combination 활용
            # group2 = tuple(district.difference(set(group1)))
            group2 = list(i for i in range(1, n + 1) if i not in group1)
            res1, res2 = check(group1), check(group2)
            if res1 and res2:
                mn = min(mn, abs(get_population(group1) - get_population(group2)))
    print(-1 if mn == float('inf') else mn)


if __name__ == "__main__":
    main()
