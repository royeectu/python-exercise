"""
Write a program to construct the following pattern, using a nested for loop
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""

for i in range(6):
    print(i * ' *')

for j in range(4, 0, -1):
    print(j * ' *')