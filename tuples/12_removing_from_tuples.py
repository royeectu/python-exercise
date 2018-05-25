# Write a program to remove an item from a tuple

my_tuple = ('a', 'b', 'c', 'd')
my_list = list(my_tuple)
my_list.remove('b')
my_new_tuple = tuple(my_list)
print(type(my_new_tuple))
print(my_new_tuple)
