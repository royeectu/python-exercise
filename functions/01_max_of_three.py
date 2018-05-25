# Write a function to find the Max of three numbers


def max_of_three(num1, num2, num3):
    if (num1 > num2) and (num1 > num3):
        return num1
    elif (num2 > num1) and (num2 > num3):
        return num2
    else:
        return num3


print(max_of_three(3, 2, 1))
print(max_of_three(2, 100, -3))
print(max_of_three(99, -5, 199))
