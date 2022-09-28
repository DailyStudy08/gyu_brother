import sys
sys.setrecursionlimit(10**9)

cnt = 1


def dfs(n):
    global cnt
    for i in adj[n]:
        answer.append(n)
        if not visited[i]:
            cnt += 1
            visited[i] = 1
            check[i] = cnt
            dfs(i)


N, M, V = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(N+1)]
visited = [0] * (N+1)
check = [0]*(N+1)
answer = []

check[V] = 1
visited[V] = 1

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)

for i in range(1, N+1):
    adj[i].sort(reverse=True)

dfs(V)

for i in range(1, N+1):
    print(check[i])
