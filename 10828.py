# https://www.acmicpc.net/problem/10828
import sys

line = int(input())

stack = []

for _ in range(line):
    order = sys.stdin.readline().split()

    if order[0] == 'push':
        stack.append(order[1])

    elif order[0] == 'pop':
        if len(stack) == 0:
            print('-1')
        else:
            pop_num = stack.pop()
            print(pop_num)

    elif order[0] == 'size':
        print(len(stack))

    elif order[0] == 'empty':
        if len(stack) == 0:
            print('1')
        else:
            print('0')

    elif order[0] == 'top':
        if len(stack) == 0:
            print('-1')
        else:
            print(stack[-1])

# line = int(input())

# stack = []
# top = -1

# for _ in range(line):
#     order = list(input().split())

#     if order[0] == 'push':
#         top += 1
#         stack.append(order[1])

#     elif order[0] == 'pop':
#         if top == -1:
#             print('-1')
#         else:
#             top -= 1
#             print(stack[top+1])


#     elif order[0] == 'size':
#         print(top+1)

#     elif order[0] == 'empty':
#         if top == -1:
#             print('1')
#         else:
#             print('0')

#     elif order[0] == 'top':
#         if top == -1:
#             print('-1')
#         else:
#             print(stack[-1])


'''
14
push 1
push 2
top
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
top

2
2
0
2
1
-1
0
1
-1
0
3
'''
