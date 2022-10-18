import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

for i in range(N-1):
    arr[i+1] += arr[i]
arr = [0]+arr

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(arr[j]-arr[i-1])
