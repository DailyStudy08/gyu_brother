sugar = int(input())
answer = 0

while sugar >= 0:
    if sugar % 5 == 0:
        answer += sugar//5
        print(answer)
        break
    sugar -= 3
    answer += 1
else:
    print(-1)

# 모든 경우를 다 조건으로 걸어주려 했는데 너무 코드가 요상해졌습니다.
# 5로 나누어 떨어질 떄 까지 3을 계속 빼줘야 한다는 것을 뒤늦게 깨닫고,, while문으로 해결했읍니다.
