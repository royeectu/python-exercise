"""
Write a program to get a string from a given string where all occurrences of its first char have been
changed to '$', except the first char itself
Sample String : 'restart'
Expected Result : 'resta$t'
"""

my_string = "restart"
char = my_string[0]
my_string = my_string.replace(char, "$")
print(char + my_string[1:])
