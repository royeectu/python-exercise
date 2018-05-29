"""
Write a program to get a single string from two given strings, separated by a space and swap the first two
characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
"""

first_string = 'abc'
second_string = 'xyz'
first_string_two_chars = first_string[0:2]
second_string_two_chars = second_string[0:2]

print(second_string_two_chars + first_string[-1] + ' ' + first_string_two_chars + second_string[-1])
