# 핵심 리프노드까지 내려와서 결과를 상향식으로 합친다
def main():
    from sys import stdin, setrecursionlimit
    setrecursionlimit(10 ** 6)
    input = stdin.readline

    def dfs(node: int) -> None:
        visited[node] = True
        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs(neighbor)
                # 리프노드까지 내려가서 확인
                dp[node][0] += dp[neighbor][1]  # 자신이 얼리어답터가 아니라면, 자식노드가 얼리어답터야 함
                dp[node][1] += min(dp[neighbor])  # 내가 얼리어답터라면 자식이 무엇이든 상관 x

    n = int(input())
    adj = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    dp = [[0, 1] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    dfs(1)
    print(min(dp[1]))


if __name__ == "__main__":
    main()
