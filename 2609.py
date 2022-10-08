def f(x, y):
    if x < y:
        x, y = y, x

    if x % y == 0:
        return y

    return f(y, x % y)


x, y = map(int, input().split())

print(f(x, y))
print(x*y//f(x, y))
