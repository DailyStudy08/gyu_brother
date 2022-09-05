N = int(input())

data = list(map(int, input().split()))

max_data = max(data)

new_list = []

for i in range(len(data)):
    new_list.append(data[i]/max_data * 100)

print(sum(new_list)/len(new_list))
