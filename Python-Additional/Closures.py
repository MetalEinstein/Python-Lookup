"""
Wikipedia definition:
A closure is a record storing a function together with an environment. The environment is a mapping
associating each free variable of the function (variables that are used locally, but defined in an enclosing scope)
with the value or reference to which the name was bound when the closure was created. Unlike a plain function,
a closure allows the function to access those captured variables through the closure's copies of their values or
references, even when the function is invoked outside their scope.

Or put more simply:
A closure is an "inner function" that remembers and have access to variables in the "outer function" in which
it was created, even if the outer function finished executing.
"""


def outer_function(msg):
    my_message = "Hi, " + msg

    def inner_function():
        # Since the "my_message" variable is not defined in this function but access is still possible it is
        # defined as a "free variable"
        print(my_message)

    return inner_function  # We return the inner function


my_func = outer_function("Rasmus")  # We pass in the "msg" argument and store the returned function in a variable
my_func()  # The function is then executed through the variable

my_func_two = outer_function("Dave")
my_func_two()
