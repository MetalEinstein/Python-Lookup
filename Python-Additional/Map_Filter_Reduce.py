

#  --- Map ---
"""
"map(func, *iterable)" allows us to in a more simple way to apply some function/operation to every
single element of a chosen number of iterables, like a list f.eks. It should be noted that the first
iterable is considered the first argument of the function passed to "map()", thus if the function you're
passing requires two, or three, or n arguments, then you need to pass in two, three or n iterables to it.
Let's make an example:
"""
my_city_names = ["aalborg", "nibe", "aarhus", "roskilde"]
print("Lower case: ", my_city_names)

# We apply the map function to our iterable. Since our "map()" function returns a generator object we use "list()"
# such that we can easily print it out
my_uppered_city_names = list(map(str.upper, my_city_names))
print("Upper case: ", my_uppered_city_names)




# --- Filter --
"""
The function, filter(), first of all, requires the function to return boolean values (true or false) and 
then passes each element in the iterable through the function, "filtering" away those that are false. 
It has the following syntax: 

filter(func, iterable)

REMEMBER:
* Only one iterable is required.

* The func argument is required to return a boolean type. If it doesn't, filter simply returns the iterable passed to it. 
  Also, as only one iterable is required, it's implicit that func must only take one argument.
  
* Filter passes each element in the iterable through func and returns only the ones that evaluate to true. 

Example:
"""
print("\n")


# We pass the elements of "my_mixed_list" to the following function and return a boolean
def find_numbers(element):
    try:  # To check if the element is a number we try to typecast it to an integer
        tmp = int(element)
        return True
    except:  # If the try failed the element must be a character or string
        return False


my_mixed_list = ["abb", 4, 2, "b", "c", 9]
print("Original list: ", my_mixed_list)

# We apply the "filter()" function to the list above
my_numbers = list(filter(find_numbers, my_mixed_list))
print("Filtered list: ", my_numbers)
