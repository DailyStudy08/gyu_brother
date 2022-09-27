import sys
sys.setrecursionlimit(10**6)

N, M, V = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)
    for i in adj:
        i.sort()


def dfs(V):
    print(V, end=" ")
    visited[V] = 1
    for i in adj[V]:
        if not visited[i]:
            dfs(i)


def bfs(V):
    stack = []
    stack.append(V)
    visited[V] = 1

    while stack:
        top = stack.pop(0)
        print(top, end=" ")

        for i in adj[top]:
            if visited[i] == 0:
                stack.append(i)
                visited[i] = 1


dfs(V)
visited = [0] * (N+1)
print()
bfs(V)
