tc = input()
a = list(map(int, input().split()))

max = -10000000
min = 10000000
for i in range(int(tc)):
    if a[i] > max:
        max = a[i]

    if a[i] < min:
        min = a[i]


print(min, max)

# 오늘 알고리즘 연습문제하고 과제를 좀 더 완벽하게 하기 위해 난이도 쉬운 걸 골랐는데
# 21분 42초 걸렸습니다. 조건에 '모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.'
# 를 안보고 max값을 0으로 해놨다가 시간을 너무 많이 잡아먹었습니다.
# 차근차근 난이도를 올려보겠습니다.
