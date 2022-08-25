a = []
for i in range(9):
    a.append(int(input()))

max_num = 0
max_idx = 0
for i in range(9):
    if a[i] > max_num:
        max_num = a[i]
        max_idx = i


print(max_num)
print(max_idx+1)