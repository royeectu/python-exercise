# Write a function that takes a list and returns a new list with unique elements of the first list


def unique_list(lst):
    temp_set = set(lst)
    return list(temp_set)


print(unique_list([1, 2, 3, 3, 3, 3, 4, 5]))
