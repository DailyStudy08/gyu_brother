import sys
sys.setrecursionlimit(10**6)


def dfs(R, depth):
    visited[R] = depth

    for i in adj[R]:
        if visited[i] == -1:
            dfs(i, depth+1)


N, M, R = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(N+1)]
visited = [-1]*(N+1)

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)

for i in range(1, N+1):
    adj[i].sort(reverse=True)

dfs(R, 0)

for i in range(1, N+1):
    print(visited[i])
