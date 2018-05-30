# Write a Python program to get the smallest number from a list

my_list = [65, -2, -5, 2, 100]
min_num = my_list[0]

for num in my_list:
    if num < min_num:
        min_num = num

print(min_num)
