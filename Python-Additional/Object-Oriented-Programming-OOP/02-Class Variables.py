class Employee:
    # Class variables/attributes. Shared by all instances of a class
    num_of_employees = 0
    raise_amount = 1.05

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + "." + last_name + "@company.com"
        # Remember that __init__ is called every time a new instance is initialized
        # The reason for assessing the "num_of_employees" through the class instead of the instance is that it
        # would be odd to have the number of employees change depending on which instance calls it.
        Employee.num_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_raise(self):
        # By accessing the class variable through the instance "self.raise_amount" we can make the raise unique
        # For each instance
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Rasmus', 'Thomsen', 30000)
emp_2 = Employee('Danny', 'Devito', 1000000)

# Applying the raise
print("Pay before raise: ", emp_1.pay)
emp_1.apply_raise()
print("With raise applied: ", emp_1.pay)

# Here the raise amount is accessed through the class. First the program checks the instance variables for the
# "raise_amount" variable. If it doesn't find it there it looks for it in the class variables
print("Raise amount: " + str(emp_1.raise_amount) + "\n")

# Lists the instance variables and their unique value. As can be seen the "raise_amount" is not
# Listed in the instance
print(emp_1.__dict__)

# Be accessing the raise_amount through the class as seen in line 22 we can set a unique raise for this particular
# instance. When we do this the class variable becomes a unique instance variable as show in the list below.
emp_1.raise_amount = 1.5
print(emp_1.__dict__)

emp_1.apply_raise()
print("Pay after additional raise: ", str(emp_1.pay) + "\n")


print("Number of employees: ", Employee.num_of_employees)



