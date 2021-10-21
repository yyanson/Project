the_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [the_list[i] for i in range(0, len(the_list)) if the_list.count(the_list[i]) < 2]
print(new_list)
