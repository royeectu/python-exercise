# Write a program to get the largest number from a list

my_list = [65, -2, -5, 2, 100]
max_num = my_list[0]

for num in my_list:
    if num > max_num:
        max_num = num

print(max_num)
