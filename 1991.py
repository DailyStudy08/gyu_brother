import sys

dic = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7}
dic1 = {'1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E', '6': 'F', '7': 'G'}


T = int(input())
l_child = [[0] for _ in range(T+1)]
r_child = [[0] for _ in range(T+1)]
for _ in range(T):
    p, l, r = sys.stdin.readline().split()
    # print(dic[p])
    l_child[dic[p]] = l
    r_child[dic[p]] = r


def preorder(n):
    if n:
        print(n)
        preorder(l_child[dic1[n]])
        preorder(r_child[dic1[n]])


a = "A"
preorder(a)
