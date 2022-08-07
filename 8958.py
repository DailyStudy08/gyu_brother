testcase = int(input())

for k in range(testcase):
    a = list(input())
    a.append('X')

    cnt = 0
    olist = []
    score = 0

    for i in a:
        if i == 'O':
            olist.append(i)
        elif i == 'X':
            for j in range(1, len(olist)+1):
                score += j
                olist = []

    print(score)

# 48분 42초 소요
# 멋져!
