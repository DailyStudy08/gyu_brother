x, y, w, h = map(int, input().split())

a = 0

if w - x < h - y:
    a = w - x

else:
    a = h - y

if a <= x and a <= y:
    print(a)

elif x <= a and x <= y:
    print(x)

else:
    print(y)
