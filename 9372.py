import sys


def dfs(node, cnt):
    visited[node] = 1
    for n in graph[node]:
        if visited[n] == 0:
            cnt = dfs(n, cnt+1)
    return cnt


for _ in range(int(sys.stdin.readline())):
    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [0]*(N+1)
    visited[1] = 0
    cnt = dfs(1, 0)
    print(cnt)
