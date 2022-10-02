def fac(n):
    if n == 0:
        return 1
    return n*fac(n-1)


a = int(input())

ans = fac(a)

print(ans)
