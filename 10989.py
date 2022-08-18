# 입력값 받아 리스트에 삽입
T = int(input())
list = []
for i in range(T):
    a = int(input())
    list.append(a)

# cnt_list 만들기 위한 빈 리스트 만들기
max = 0
for x in list:
    if x > max:
        max = int(x)

cnt_list = [0] * (max+1)

# 각 요소 갯수 세기
for i in range(len(list)):
    cnt_list[list[i]] += 1

# 누적으로 바꾸기
for k in range(1, max+1):
    cnt_list[k] += cnt_list[k-1]

# 새로 정렬될 new_list4


new_list = [-1] * len(list)

for j in range(len(list)):
    cnt_list[list[j]] -= 1
    new_list[cnt_list[list[j]]] = list[j]

for i in new_list:
    print(i)


# 과제가 너무 늦게 끝나 공부도 할 겸 + 했던 정렬이라 복습도 할 겸 골랐는데
# 어려워서 한 시간 반 이상 소요했습니다.
# **counting sort를 겨우 만들었는데,, 채점이 되지 않습니다. 너무 머리가 아파 일단 여기까지 하고 제출합니다.
