import sys


T = int(input())
queue = []

for _ in range(T):
    order = sys.stdin.readline().split()

    if order[0] == 'push':
        queue.append(int(order[1]))

    elif order[0] == 'pop':
        if not queue:
            print('-1')
        else:
            print(queue.pop(0))

    elif order[0] == 'size':
        print(len(queue))

    elif order[0] == 'empty':
        if not queue:
            print('1')
        else:
            print('0')

    elif order[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print('-1')

    elif order[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print('-1')
