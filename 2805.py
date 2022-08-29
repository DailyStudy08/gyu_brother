import sys

N, M = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
start = 0
end = max(data)

while start <= end:             # 이분탐색 시작
    mid = (start+end)//2
    tree_sum = 0
    for i in data:                  # 자르고 남은 나무 길이 먼저 제기
        if i >= mid:
            tree_sum += i - mid

    if tree_sum < M:
        end = mid - 1

    if tree_sum >= M:
        start = mid + 1

print(end)
