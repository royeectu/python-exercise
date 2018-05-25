# Write a program to find maximum and the minimum value in a set

# Let's create a set:
my_set = {-3, 0, 99, 1000, -9}

# Let's find the minimum value:
minimum = 0
for i in my_set:
    if i < minimum:
        minimum = i

print(f"The minimum number in the set is: {minimum}")

# Let's find the maximum value:
maximum = 0
for i in my_set:
    if i > maximum:
        maximum = i

print(f"The maximum number in the set is: {maximum}")
