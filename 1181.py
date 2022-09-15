T = int(input())
words = []
for _ in range(T):
    words.append(input())

result = list(set(words))
result.sort()
result.sort(key=len)

for i in result:
    print(i)
