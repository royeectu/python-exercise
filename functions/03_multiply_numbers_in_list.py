# Write a function to multiply all the numbers in a list


def multiply_in_list(num_list):
    total = 1
    for num in num_list:
        total *= num
    return total


print(multiply_in_list([8, 2, 3, -1, 7]))
