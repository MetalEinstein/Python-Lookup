"""
When dealing with large data-sets it is often the case that large sums of memory is unnecessarily occupied by
the program. Furthermore storing and retrieving from memory takes additional time.

This is were the "generator" comes in. By not storing the data in memory and only processing one value at a time
so to say the program saves not only on memory but also time
"""

# How it would normally be done
"""
def squared_numbers_generator(nums):
    result = []
    for num in nums:
        result.append(num*num)
    return result
"""

# We create a list with numbers 1-10
my_nums = [i for i in range(1, 11)]


# The generator is created through the "yield" function. It doesn't store the values processed in memory (in a list) but
# rather returns them one at a time
def squared_numbers_generator(nums):
    for num in nums:
        # Each number in our number list is squared and returned on at a time. A generator "remembers" where it left
        # off meaning that the next time we call the function it processes the next number in the list
        yield num*num


# "my_squared_nums" is a generator object meaning that we have to loop through it to get all the numbers
# Remember that it processes it one value at a time instead of returning an entire list
my_squared_nums = squared_numbers_generator(my_nums)
for i in my_squared_nums:
    print(i)
