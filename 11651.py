import sys

N = int(input())
lst = []
for _ in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    lst.append(a)

lst.sort(key=lambda x: (x[1], x[0]))

for i in lst:
    print(i[0], i[1])
