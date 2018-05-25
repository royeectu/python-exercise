# Write a  program to remove item(s) from set

# Let's create a set:
my_set = {1, 2, 3, 4, 5, 6, 7, 8}
print(my_set)

# Let's remove an element from the set:
my_set.remove(3)
print(my_set)

# Let's remove another element:
my_set.remove(1)
print(my_set)

# If we try to remove a non existing element, we will get a KeyError. Let's remove only if an element exists:
if 7 in my_set:
    my_set.remove(7)

print(my_set)

# If we use the discard method we can safely remove elements even if they don't exist in the set:
my_set.discard(-1000)

# We can also use pop:
my_set.pop()
print(my_set)
