N, M = map(int, input().split())
visited = [0]*(N+1)
ans = []


def f(idx):
    if idx == M:
        if ans == sorted(ans):
            print(*ans)

    for i in range(1, N+1):
        if visited[i] == 0:
            visited[i] = 1
            ans.append(i)
            f(idx+1)
            visited[i] = 0
            ans.pop()


f(0)
