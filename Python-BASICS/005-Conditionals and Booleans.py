# Comparisons operators:  (Will return boolean)
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2
# Object identity:    is -> A bit complicated. Will be explained below

print("------------------------------- if, elif, else ---------------------------------")

# If language is equal to 'Python' we do something -> Makes a lot of sense
language = 'Python'
if language == 'Python':
    print("We are writing in Python")

# We can also implement reactions to multiple outcomes using 'elif' and 'else'.
language2 = 'Java'
if language2 == 'Python':
    print("We are writing in Python")

elif language2 == 'Java':
    print("We are writing in Java")

elif language2 == 'C++':
    print("We are writing in C++")

else:
    print("Language not detected")

print("\n------------------------------- and, or, not ---------------------------------")

# Let's do some boolean algebra
A = 0
num = 1

# and
if A == 0 and num == 1:  # If A = 0 and B = 1 do something
    print("A * 1 = A")

# or
if A or num == 1:  # If A or num is equal to 1 do something
    print("A + 1 = 1")

# not
"""
'not' inverts the specified variable. Thus A inverts from 0 to not 0 and every number besides 0 is registered as 
'True'. So the following code should be read as: 
if True:
     print("not A = A is not zero")
"""
if not A:
    print("A * not_A = 0 * 1 = 0")


print("\n------------------------------- Evaluating to true or false ---------------------------------")
# False Values: -> Any variable set to the following will register as 'False'. Everything else will be 'True'
# False
# None
# Zero of any numeric type
# Any empty sequence. For example, '', (), [].
# Any empty mapping. For example, {}.

"""
One of the primary uses of this type of coding is to check if something is empty and act accordingly. Don't want to
continue in the program with non-existing data.   
"""

# False
condition = False
if condition:  # Same as saying: if condition is True
    print("Evaluated to True")
else:
    print("Evaluated to False")

# None
condition2 = None
if condition2:  # Same as saying: if condition is True
    print("Evaluated to True")
else:
    print("Evaluated to False")

# Zero of any numeric type
condition3 = 0
if condition3:  # Same as saying: if condition is True
    print("Evaluated to True")
else:
    print("Evaluated to False")

# Any empty sequence. For example, '', (), [].
empty_list_example = []
if empty_list_example:  # Same as saying: if condition is True
    print("Evaluated to True")
else:
    print("Evaluated to False")


print("\n------------------------------- Using the 'is' statement ---------------------------------")
"""
The 'is' statement checks for the objects identity in memory. If two object are different (even if they contain the
same data) the 'is' statement returns 'False'. Otherwise it returns 'True'
"""
# Example 1 -> Here 'is' will return False
a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))
print(id(b))

if a is b:
    print("a and b is the same object")
else:
    print("a and b are not the same object")

print("\n")

# Example 2 -> Here 'is' will return True
c = [1, 2, 3]
d = c
print(id(c))
print(id(d))

if c is d:
    print("a and b is the same object")
else:
    print("a and b are not the same object")

