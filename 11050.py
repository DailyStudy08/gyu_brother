def fac(n):
    if n <= 1:
        return 1
    else:
        return n*fac(n-1)


N, K = map(int, input().split())

answer = fac(N)//(fac(N-K)*fac(K))

print(int(answer))
