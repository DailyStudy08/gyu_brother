a = int(input())
b = input()

for n in range(len(b), 0, -1):
    print(a*int(b[n-1]))

print(a*int(b))
