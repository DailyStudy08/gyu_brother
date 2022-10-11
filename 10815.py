import sys


def binary_search(goal, check_list, start, end):
    # 종료 조건
    if start > end:
        return 0

    mid = (start+end)//2

    if goal == check_list[mid]:
        return 1

    elif goal < check_list[mid]:
        end = mid - 1

    elif goal > check_list[mid]:
        start = mid + 1

    return binary_search(goal, check_list, start, end)

# <<<<set>>>>
# N = int(input())
# check_lst = set(sys.stdin.readline().split())
# int(input())

# for i in list(sys.stdin.readline().split()):
#     if i in check_lst:
#         print('1', end=" ")
#     else:
#         print('0', end=" ")


# <<<< 이진탐색 >>>>>
N = int(input())
check_lst = sorted(sys.stdin.readline().split())
int(input())

for i in list(sys.stdin.readline().split()):
    print(binary_search(i, check_lst, 0, N-1), end=" ")


# set로 하는게 훨씬 빠르네융,,
