# Write a program to find the repeated items of a tuple

my_tuple = (1, 2, 3, 4, 5, 6, 6, 6, 6, 0, 1)

# 1st solution:
count = 0

for i in my_tuple:
    if i == 6:
        count += 1

print(count)

# 2nd solution:
print(my_tuple.count(1))
