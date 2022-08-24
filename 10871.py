N, pivot = map(int, input().split())
sample = list(map(int, input().split()))

for i in sample:
    if i < pivot:
        print(i, end=' ')
