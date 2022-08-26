# https://www.acmicpc.net/problem/2798

N, M = map(int, input().split())
data = list(map(int, input().split()))

sum = []
for i in range(len(data)):
    for j in range(i+1, len(data)):
        for k in range(j+1, len(data)):
            sum.append(data[i]+data[j]+data[k])
min = 0xfffff

for i in sum:
    if M - i >= 0 and M - i < min:
        min = M - i

print(M - min)

# n = len(data)
# set = []
# for i in range(1 << n):
#     subset = []
#     for j in range(n):
#         if i & (1 << j):
#             subset.append(data[j])
#     set.append(subset)

# sample = []
# min = 0xfffff

# for i in range(len(set)):
#     if len(set[i]) == 3:
#         if M - sum(set[i]) >= 0 and M - sum(set[i]) <= min:
#             min = sum(sample[i])

# print(min)
