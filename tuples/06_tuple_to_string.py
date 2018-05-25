# Write a program to convert a tuple to a string

my_tuple = ('h', 'e', 'l', 'l', 'o')

# 1st solution:

my_str = ""

for letter in my_tuple:
    my_str += letter

print(my_str)

# 2nd solution:

print("".join(my_tuple))
