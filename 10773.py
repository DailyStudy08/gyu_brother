N = int(input())
data = []
answer = []
for i in range(N):
    data.append(int(input()))

for i in range(N):
    if data[i] != 0:
        answer.append(data[i])

    else:
        answer.pop()

print(sum(answer))
