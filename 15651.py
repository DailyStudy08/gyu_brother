N, M = map(int, input().split())
ans = []


def f(idx):
    if idx == M:
        print(*ans)
        return

    for i in range(1, N+1):
        ans.append(i)
        f(idx+1)
        ans.pop()


f(0)
