a_num = int(input())
a_list = sorted(list(map(int, input().split())))
b_num = int(input())
b_list = list(map(int, input().split()))


def binarySearch(a, N, key):
    start = 0
    end = N - 1
    while start <= end:
        middle = (start + end)//2
        if a[middle] == key:
            return 1
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return 0


for i in b_list:
    print(binarySearch(a_list, a_num, i))
