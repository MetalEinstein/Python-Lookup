"""
Try Except:
* Is used for catching errors and handling them in a specific way
  - Let's make whats called a "try block". It tests out a specified piece of code trying to catch any errors before
    it enters the main program.
  - Remember to be specific about the error you are trying to catch. Just typing "except:" is gonna be too broad a
    search.
"""


try:  # Try the piece of code below
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result of 10/" + str(number) + ":", result)


# The "except" is used to search for a specific error, in this case a "division by zero" error that could be caused by
# the value of "answer"
except ZeroDivisionError as err:  # We save the error "as" err in order to print it out
    print(err)

# In the line below we are looking for a value error that could occur if we enter a character/string instead of a
# number
except ValueError as errTwo:
    print(errTwo)
