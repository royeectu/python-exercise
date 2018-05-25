# Write a function to sum all the numbers in a list


def sum_in_list(num_list):
    total = 0

    for num in num_list:
        total += num
    return total


print(sum_in_list([8, 2, 3, 0, 7]))
