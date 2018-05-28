# Write a script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

n = 5

my_dcit = { num:num ** 2 for num in range(n + 1)}
print(my_dcit)
