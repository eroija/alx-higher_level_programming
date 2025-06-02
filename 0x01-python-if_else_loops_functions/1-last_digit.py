#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Get the last digit (absolute value to handle negative numbers)
last_digit = abs(number) % 10

# Print the result with appropriate condition
print("Last digit of {} is {}".format(number, last_digit), end="")

if last_digit > 5:
    print(" and is greater than 5")
elif last_digit == 0:
    print(" and is 0")
else:  # last_digit < 6 and last_digit != 0 (which means 1, 2, 3, 4, or 5)
    print(" and is less than 6 and not 0")
