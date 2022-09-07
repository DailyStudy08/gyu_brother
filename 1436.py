N = int(input())
answer = 0
num = 0

while True:
    if '666' in str(num):
        answer += 1

    if answer == N:
        print(num)
        break

    num += 1
