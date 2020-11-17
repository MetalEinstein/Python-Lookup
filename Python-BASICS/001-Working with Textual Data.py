"""
This tutorial will cover the basics of working with textual data. It will cover:
* Quotation
* Accessing individual string characters and ranging/slicing
* Some useful string functions
* Stringing strings together and using Formatted strings
* Helper functions
"""

# -------------- Quotation---------------------
print("----------------------------Quotation-----------------------------------")
message_a = 'Single quotes/quotations can be used to type in a message'
message_b = "And so can double quotes"

print(message_a)
print(message_b)
print("\n")  # Newline

# You do the following in order not to confuse the compiler
message_c = "However if you want to use single quotes in a message you use double quotes. Example: Bobby's Pizza"
message_d = 'And if you use double quotes in a message you frame the message in single quotes'

print(message_c)
print(message_d)
print("\n")

message_e = """You can also use triple quotation to make a newline
inside of your message after jumping to a new line with 'Enter'"""

print(message_e)
print("\n")


# -------------- Accessing individual string characters and ranging---------------------
print("-------------------------Accessing individual string characters and ranging--------------------------------")

# You can think of a line a text as a array of characters "stringed" together to form a ord or sentence
message_f = "Hallo World"

# Use the '[]' brackets to specify the index location of a specific character in the array
print(message_f[0])  # The character "H" in the message is located at index location '0'
print("\n")

# If you want to print out more than one character you can use a technique called "Ranging/Slicing"
print(message_f[0:5])
"""
The above code will print all characters from index location 0-4. 0:5 should be read as: Access everything from index
location 0 up to but not including 5
"""

print(message_f[:5])  # Does the same as the one above

print(message_f[6:])  # Will print all characters from index location 6-end

# Negative values can also be used to access the back of the string/array
print(message_f[-1])
# Applied to ranging
print(message_f[-5:])  # Will print out what's stored in the last 5 parts of the string

# We can also choose a step size. Let's say we want to print every second word in our string:
print(message_f[::2])
"""
The above code should be read as: Start from 0 and go to the end 2 steps at a time. We can also step backwards
like this:
"""
print(message_f[::-1])  # Will print out the string backwards
print("\n")


# -------------- Some useful string functions---------------------
print("----------------------------Some useful string functions-----------------------------------")

message_g = "Peter is a hypochondriac"

# Some useful string functions are:
print(len(message_g))  # Will print the length of the string

print(message_g.lower())  # Will print the string in all lower case
print(message_g.upper())  # Will print the string in all upper case
print(message_g[0].islower())  # Will check if the first character is uppercase (Returns boolean)
print(message_g[0].isupper())  # Will check if the first character is lowercase

print(message_g.count("Peter"))  # Will return the number of times a string or character appears in the message

print(message_g.find("r"))  # Finds the index location of the first instance of the character 'r'
print(message_g.find("hypochondriac"))  # Finds the starting location of the specific string

new_message = message_g.replace("Peter", "Olga")
print(new_message)
"""
The above function will replace the name Peter in the original message and replace it with the name Olga. Remember to
define a new variable (new_message) since it's a return function. The original message is not overwritten. 
"""

# String functions can also be combined together
print(message_g.upper().isupper())  # Will convert message to uppercase and check if it's uppercase. :D
print("\n")


# -------------- Stringing strings together and Formatted strings---------------------
print("----------------------------Stringing strings together and Formatted strings-----------------------------------")

# The '+' sign can be used to add strings together like so:
greeting = "Hallo"
name = "John"

print(greeting + ", " + name)

"""
Now as might can imagine a very complicated message can be hard to read in code when you have to keep track of all the
',' and '+' and so on. To solve this problem we can use a formatted string like so: 
"""
# Formatted string:
message_h = '{}, {}'.format(greeting, name)  # The messages will be placed in the placeholders '{}' in sequence
print(message_h)
print("\n")


# -------------- Helper functions---------------------
print("----------------------------Helper functions-----------------------------------")

"""
Now since there is a lot of functions available for each data-type it can be hard to keep track of them all.
We can therefore use the following functions to get a overview and even details 
"""

end_message = "John"
print(dir(end_message))  # Will print all available functions for this variable (General overview)
print("\n")
print(help(str))  # Will print details about every function related to strings (str)
print(help(str.lower))  # Will print details about a specific string function. In this case '.lower'
