
print("------------------------------- For-loops ---------------------------------")
nums = [1, 2, 3, 4, 5]

# Simple for-loop
print("Product of simple for-loop:")
for num in nums:  # For each data variable in 'nums' do something
    print(num)

print("\n--- break and continue ---")

# for-loop with break
print("With break:")
for num in nums:
    if num == 3:  # if num = 3 we break out of the loop
        break
    print(num)

print("\n")

# for-loop with continue
print("With continue:")
for num in nums:
    if num == 3:
        print("You have reached the number 3")
        continue  # With "continue" the loop keeps going after a specified action have been performed
    print(num)


print("\n--- nested for-loop ---")

print("Product of nested for-loop:")
"""
For each primary loop the code with enter a secondary loop. When the secondary loop is finished it will go back
to the primary loop. Rinse and repeat until the primary loop has reached the last data-point.
"""
for num in nums:
    for letter in 'abc':
        print(num, letter)


print("\n--- ranged for-loop ---")

print("Product of ranged for-loop")
# The following will print all numbers from 0 to but not including 10
for num in range(10):
    print(num)

# A starting number can also be chosen
print("\nranged for-loop with starting number:")
for num in range(1, 11):
    print(num)


print("\n------------------------------- while-loops ---------------------------------")
"""
A while-loop with keep going until a break is initiated or a specified condition is met 
"""
print("Iterative while-loop with condition:")
x = 0
while x < 5:
    print(x)
    x += 1  # Same as saying x = x + 1


print("\nIterative while-loop with break:")
x = 0
while True:  # This will create an infinite loop without the 'break'
    if x == 6:
        break
    print(x)
    x += 1
