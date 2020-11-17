"""
* When thinking about functions think about a machine that takes in one or multiple resources, processes them
and returns a product.

* When writing a function it is good practice to write a note/doc string that simply explains what the function
does. The structure should be as follows:

def function():
    "write the note here"
    code
    code
    code
"""
print("------------------------------- Functions ---------------------------------")
print('--- Simple functions ---')


def print_string():  # We def (define) a function name and specify what it should do
    print("Hallo there")


print("Product of simple print function:")
print_string()  # Here we call the function by calling the specified name


# We can also just return a string
def return_string():
    return 'I come from a foreign land'


print("\nProduct of the string return function:")
print(return_string())


print('\n--- Argument functions ---')


def my_argument_function(name, study):  # We define two arguments (name and study)
    return "Hallo there {}, i hope its going well at {}".format(name, study)


print("Product of argument function:")
print(my_argument_function('Rasmus', 'Robotics'))  # We pass in the two arguments to the function


# If we don't always have a argument to pass in to a function we can specify a default value
def function_with_default(name_default='user'):
    return 'Hallo {}, i hope you are having a nice day'.format(name_default)


print("\nProduct of function with default argument:")
print(function_with_default())  # Without passing in the argument. Will use default value
print(function_with_default('Rasmus'))  # Passing in a argument
