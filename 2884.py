h, m = map(int, input().split())

if h == 0:
    if m < 45:
        print(f'{23} {60+m-45}')
    else:
        print(f'{h} {m-45}')

else:
    if m < 45:
        print(f'{h-1} {60+m-45}')
    else:
        print(f'{h} {m-45}')
