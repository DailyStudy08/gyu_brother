A, B, V = map(int, input().split())

if (V-B) % (A-B) == 0:
    print(int((V-B)/(A-B)))
else:
    print(int((V-B)//(A-B)+1))

# height = 0
# cnt = 0
# while True:
#     height += A
#     cnt += 1

#     if height >= V:
#         break

#     height -= B

# print(cnt)
