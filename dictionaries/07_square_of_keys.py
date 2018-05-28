'''
Write a script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are
square of keys
'''

my_dict = { num: num **2 for num in range(16)}
print(my_dict)
