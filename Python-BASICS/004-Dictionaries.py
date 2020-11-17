"""
* A term important to understanding dictionary's is 'key-value pairs'. It simply means that a value can be
accessed though the use of a input key. The values differ depending on the key.

* It is also important to mention that dictionaries are mutable (can be changed)
"""
print("---------------------------- Dictionaries -----------------------------------")
print('--- A simple set of examples ---')

# A dictionary can be created by using '{}'
student_info = {'name': 'Rasmus', 'age': 25, 'study': 'Robotics'}  # key is 'name' and value is 'Rasmus'

# Remember that the key is passed in '[]' brackets
message = '{} is {} years old and studies {}'.format(student_info['name'], student_info['age'], student_info['study'])
print(message)


print('\n--- Updating and deleting ---')

# While keys and values can be updated individually, it's better to use the update function
print("Product of updating:")
student_info.update({'name': 'John', 'age': 27, 'study': 'Chemistry'})

message = '{} is {} years old and studies {}'.format(student_info['name'], student_info['age'], student_info['study'])
print(message)

# We can also delete a key-value pair
print("\nProduct of deleting:")

del student_info['study']
print(student_info)


print('\n--- Getting keys, values and key-value pairs ---')

# Sometimes it can be useful to see whatever the dictionaries contains
print("Getting keys:")
print(student_info.keys())

print("\nGetting values:")
print(student_info.values())

print("\nGetting key-value pairs:")
print(student_info.items())

# We can also loop though the keys and values
print("\n")
for keys, value in student_info.items():  # Remember, items() returns both a key and a value
    print(keys + ":", value)
