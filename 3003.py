chess = [1, 1, 2, 2, 2, 8]

my_chess = list(map(int, input().split()))

result = []
for i in range(6):
    result.append(chess[i] - my_chess[i])

print(*result)
