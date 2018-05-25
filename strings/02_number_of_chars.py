# Write a program to count the number of characters (character frequency) in a string

my_str = "google.com"

my_dict = {char: my_str.count(char) for char in my_str}
print(my_dict)
