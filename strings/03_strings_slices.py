"""
Write a program to get a string made of the first 2 and the last 2 chars from a given a string.
If the string length is less than 2, return instead of the empty string
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String
"""

input_string = 'w3'


def string_len(string):
    if len(string) < 2:
        return "Empty String"
    return string[0:2] + string[-2:]


print(string_len(input_string))
