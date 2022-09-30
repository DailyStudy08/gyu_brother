import sys
sys.setrecursionlimit(10**6)


def dfs(n, deep):
    visited[n] = deep

    for i in adj[n]:
        if visited[i] == -1:
            dfs(i, deep+1)


N, M, V = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(N+1)]
visited = [-1] * (N+1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)

for i in range(1, N+1):
    adj[i].sort()

dfs(V, 0)

for i in range(1, N+1):
    print(visited[i])
