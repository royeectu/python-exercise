# Write a program to calculate the length of a string

my_str = "I love Docker"

# 1st solution:
print(len(my_str))

# 2nd solution:
count = 0

for char in my_str:
    count += 1

print(count)
