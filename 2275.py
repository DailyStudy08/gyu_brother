# tc = int(input())

# for k in range(tc):
#     base = list(range(1, 15))
#     upper_story = base
#     K = int(input())
#     N = int(input())
#     for j in range(0, K):

#         story = upper_story[:]
#         upper_story = []
#         sum = 0 

#         for i in range(1, 15):
#             sum += story[i-1]
#             upper_story.append(sum)

#     print(upper_story[N-1])
#     위 코드 추가적으로 고민이 필요한 것 같습니다. 꽤오래걸림,,

tc = int(input())

for i in range(tc):
    lst = []
    lst.append(list(range(1, 16)))

    k = int(input())  # 층
    n = int(input())  # 호수
    for j in range(1, k+1):
        tmp = [1]
        for m in range(1, n+1):
            tmp.append(lst[j-1][m]+tmp[m-1])
        lst.append(tmp)

    print(lst[k][n-1])
