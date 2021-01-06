"""
Remember:
* A lambda function is a small anonymous function.

* A lambda function can take any number of arguments, but can only have one expression.

* The lambda function has the following syntax:

lambda arguments : expression

Example:
"""

# Simple example
x = lambda a: a + 10
print(x(5))  # We pass in "5" as our argument


print("\n")


# With more than one argument
y = lambda a, b: a + b
print(y(4, 6))


print("\n")


# When nested in a normal function.
# Through this method we can return custom functions on the fly
# In this case we pass in the value of 'n' that we wish to multiply with a specified number 'a'
def multiplier(n):
    return lambda a: a * n  # We return the function


doubler = multiplier(2)  # We want to multiply by number two
print(doubler(2))  # We pass in the number we wish to double

tripler = multiplier(3)  # If we want to multiply by 3
print(tripler(2))



