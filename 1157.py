word = str(input())

word_upper = list(word.upper())

word_set = set(word_upper)

word_count_dict = {}

for i in word_set:
    word_count_dict[i] = word_upper.count(i)

count_list = []

for i in word_count_dict.values():
    count_list.append(i)

count_list.sort(reverse=True)

for j, k in word_count_dict.items():

    if count_list[0] == 1:
        print(j)

    elif count_list[0] == count_list[1]:
        print('?')
        break

    elif k == count_list[0]:
        print(j)
