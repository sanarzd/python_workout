list_of_lists = [[1, 2, 3], [0], [4, -4, 5], [10]]
sorted_list = sorted(list_of_lists, key=sum)
print(sorted_list)  