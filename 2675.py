T = int(input())
for i in range(T):
    data = input().split()
    a = int(data[0])

    for i in range(len(data[1])):
        print(a*data[1][i], end='')
    print()
