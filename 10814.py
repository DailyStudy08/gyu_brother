import sys

N = int(input())
b = []

for _ in range(N):
    a = sys.stdin.readline().split()
    b.append(a)

b.sort(key=lambda x: (int(x[0])))

for i in b:
    print(*i)
