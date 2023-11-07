# Program to calculate factorial of a number
number = 5
factorial = 1

if number == 0:
    factorial = 1

else:
    while number > 0:
        factorial = factorial * number
        number = number - 1

print(factorial)
