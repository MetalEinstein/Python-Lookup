"""
This tutorial will cover:
* Arithmetic Operators
* Incrementation
* Some numeric functions
* Comparison operators
* Converting numbers to strings and strings to numbers (Casting)
"""


print("------------------------------- Arithmetic Operators ---------------------------------")
# Arithmetic Operators:
# Addition:       3 + 2
# Subtraction:    3 - 2
# Multiplication: 3 * 2
# Division:       3 / 2
# Floor Division: 3 // 2 - Drops to lowest decimal
# Exponent:       3 ** 2
# Modulus:        3 % 2 - Returns the remainder

print(3 + 2)
print(3 - 2)
print(3 * 2)
print(3 / 2)
print(3 // 2)
print(3 ** 2)
print(3 % 2)

print("\n")


print("------------------------------- Incrementation ---------------------------------")

num = 1

# We can increment in two ways:
num = num + 1  # Now it's 2
# Or
num += 1  # Does the same but takes less space. Now it's 3

print(num)

print("\n")


print("------------------------------- Some numeric functions ---------------------------------")

print(abs(-3))  # Takes the absolute value

print(round(3.75))  # Rounds to the closest digit
print(round(3.75, 1))  # Rounds to the closest digit after the FIRST decimal

print(min(4, 6, 8, 7))  # Returns the smallest number in a set
print(max(4, 6, 8, 7))  # Returns the biggest number in a set

print("\n")


print("------------------------------- Comparison operators ---------------------------------")
# Comparisons operators:  (Will return boolean)
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2

num1 = 3
num2 = 2

print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)

print("\n")


print("---------------------------- Converting numbers to strings and strings to numbers------------------------------")

# Two numbers as strings
num1 = "100"
num2 = "200"

# Casting to integers
num3 = int(num1) + int(num2)  # Casting to integers and adding them together
print("{} + {} is equal to: {}".format(num1, num2, num3))  # Printing the result using a formatted string

# Casting to string
string_num = str(num3)
print(string_num + " is a odd but awesome movie")
"""
In order to print a number together with strings we will first need to convert the number to a string as seen
above. 
"""
