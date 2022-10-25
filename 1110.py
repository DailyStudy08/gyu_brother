# n = input()
# num = n
# cnt = 0

# while True:
#     if len(n) == 1:
#         num = '0'+num

#     sum = str(int(num[0])+int(num[1]))
#     num = num[-1] + sum[-1]
#     cnt += 1

#     if num == n:
#         print(cnt)
#         break


n = int(input())
num = n
count = 0

while True:
    a = num//10
    b = num % 10
    c = (a+b) % 10
    num = (b*10) + c
    count += 1
    if(num == n):
        break

print(count)
