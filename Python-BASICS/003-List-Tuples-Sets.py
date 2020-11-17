"""
This tutorial will cover:
* Lists
* Some list methods/functions
"""

print("----------------------------Lists-----------------------------------")

# A list can be created in the following way:
first_list = ['John', 'Michale', 'Jacob']
print(first_list)

# Like shown in Tutorial 01 we can access individual list elements using a index number
print(first_list[0])
print(first_list[1])

# Or we could print a range of list elements (Ranging is covered in Tutorial 01)
print(first_list[0:2])

print("\n")


print("----------------------------Some list methods/functions-----------------------------------")
print("---ADDING---")

# To add something to the end of a list use the following function:
first_list.append('Chris')
print(first_list)

# To place something at a specified location you can use "insert" instead:
first_list.insert(0, 'Palle') # Inserts "Palle" at location 0
print(first_list)

# An new list can also be added to an existing list making it a nested list (using insert again)
new_list = ['Sarah', 'Peter', 'Lars']

first_list.insert(0, new_list)
print(first_list)  # Notice that an entire list is now inside another list (nested list)
print(first_list[0])  # Prints the entirety of the new list we inserted at location 0
print(first_list[0][0])  # Prints the first element of the inserted list

# To avoid placing an entire list inside another the "extend" method is used instead
list_to_extend = ['Mathilde', 'Pulle', 'Mulle']

list_to_extend.extend(new_list)
print(list_to_extend)  # Notice that the elements of "new_list" are added to the end of the list

print("\n---Removing---")

# To remove something specific
print(list_to_extend)

list_to_extend.remove("Mulle")  # We look for and remove the string "Mulle"
print(list_to_extend)

# To remove something from the end of the list we use 'pop' instead
list_to_extend.pop()
popped_element = list_to_extend.pop()  # 'pop()' also returns the popped element such that we can store it
print(list_to_extend)
print(popped_element)  # Prints the popped element

print("\n ---Manipulating the list--- ")

# A list can be reversed using the following function
list_to_manipulate_string = list_to_extend
print(list_to_manipulate_string)

list_to_manipulate_string.reverse()
print(list_to_manipulate_string) # As can be seen the list is now reversed

# A list can also be sorted. This works for both numbers and strings
alphabet_list = ["Albert", "Bert", "Charlie"]
list_to_manipulate_string.extend(alphabet_list)

list_to_manipulate_string.sort()  # The list is sorted according to alphabetic order
print(list_to_manipulate_string)

list_to_manipulate_number = [1, 4, 8, 7, 5]
list_to_manipulate_number.sort()  # Here the numbers are sorted from lowest to highest
print(list_to_manipulate_number)

list_to_manipulate_number.sort(reverse=True)  # And here the numbers are sorted from highest to lowest
print(list_to_manipulate_number)

# If we don't want to change the original list we can instead use the 'sorted' function
sorted_list = sorted(list_to_manipulate_number)
print(sorted_list)

print("\n--- min, max, sum and index location ---")
print(sorted_list)

# Finding the min, max and sum of a list
print("min = ", min(sorted_list))
print("max = ", max(sorted_list))
print("sum = ", sum(sorted_list))

# Finding the index location of a input string or variable
print(sorted_list.index(7))

print("--- List to string and string to list ---")

"""
A list can be converted to a set of strings by printing out the individual elements of the list separated 
by a specified character like ' - ' or ' + ' or something else. However a string can also be converted to 
a list by separating the individual elements. We have to specify what separates the elements tho, like a space 
or a comma f.eks. 
"""
print(list_to_manipulate_string)

# List to string
list_to_string = ' - '.join(list_to_manipulate_string)
print(list_to_string)  # As can be seen the elements of the list are printed out separated by ' - '

# string to list
string_to_list = list_to_string.split(' - ')  # We split the elements up based on ' - '
print(string_to_list)


print("\n----------------------------Tuples-----------------------------------")
"""
Before we start there are two terms in programming we need to cover, those being "Mutable" and "Immutable"

Mutable:
Means that the object (like a list) can be changed after being created 

Immutable:
Means that the list can't be changed after creation. Tuples are Immutable. 

To illustrate the usefulness of of immutable object an example of a problem with mutable problem is show below:
"""
# Mutable problem
list_1 = ["Albert", "Betty", "Charlie"]
list_2 = list_1
print(list_1)
print(list_2)

list_1[0] = "Dani"  # The first element of the first list is changed to "Dani"

print(list_1)
print(list_2)
"""
As can be seen in the prints above, changing the first list also changes the second since list_2 = list_1.
For some more complex programs or applications this might pose a problem. However by using a Tuple we can 
avoid this issue since a tuple can't be changed and will therefore trow an error if a change is attempted.  
"""

# Immutable
tuple_1 = ("Albert", "Betty", "Charlie")  # Notice that we are using parentheses "()" instead of brackets "[]"
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)

# tuple_1[0] = "Dani" -> This will trow an error
# print(tuple_1)
# print(tuple_2)


print("\n----------------------------Sets-----------------------------------")
"""
"Sets" are values that are unordered and also have no duplicates. They are often used to remove duplicates
in a dataset or to check if a element is part of a set. 
"""
# Sets -> Notice that every time we run the program the elements of the sets changes place (unordered)
str_set = {"Charlie", "Charlie", "Albert", "Albert", "Simon"}  # Notice that we are using the "{}" brackets
num_set = {1, 1, 1, 8, 5, 2, 5, 9, 10, 4}
print(str_set)
print(num_set)

print("\n--- Intersection, Difference and Union ---")
set_1 = {1, 2, 3, 7, 8, 9, 10}
set_2 = {3, 4, 5, 6, 7}
# The following are 3 ways to compare sets:

# Intersection -> What is in both A and B
print(set_1.intersection(set_2))

# Difference -> What is in A but not in B
print(set_1.difference(set_2))

# Union -> What is in either A or B or in both A and B. Will just join the two sets
print(set_1.union(set_2))


print("\n----------------------------How to create empty Lists, Tuples and Sets-----------------------------------")

# 2 Ways to create a empty list:
empty_list = []
empty_list = list()

# 2 Ways to create a empty tuple
empty_tuple = ()
empty_tuple = tuple()

# A single way to create a empty set
empty_set = {}  # <- This is wrong. It will create a empty dictionary
empty_set = set()  # This will work
