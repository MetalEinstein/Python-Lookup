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


# The class "Developer" inherits all variables and methods from the "Employee" class
# However we can define new variables and methods unique to this subclass along with overwriting existing ones
class Developer(Employee):
    raise_amount = 1.5  # This class variable is overwritten such that it is unique for this subclass

    def __init__(self, first_name, last_name, pay, prog_lang):
        # "super" passes first_name, last_name and pay to the Employee class so they can't be handled there
        # Our Developer class only needs to handle "prog_lang"
        super().__init__(first_name, last_name, pay)
        self.prog_lang = prog_lang  # We define a new instance variable unique to this class


# We call the new subclass and pass in the instance variables
emp_1_dev = Developer('Rasmus', 'Thomsen', 30000, 'Python')

print("Full Name: {},    Programming language: {},    Pay: {}".format(emp_1_dev.fullname(), emp_1_dev.prog_lang, emp_1_dev.pay))
emp_1_dev.apply_raise()
print("Full Name: {},    Programming language: {},    Pay after raise: {}".format(emp_1_dev.fullname(), emp_1_dev.prog_lang, emp_1_dev.pay))

print("\nHelper functions, isinstance and issubclass:")
print("Is emp_1_dev an instance of the Developer class?: " + str(isinstance(emp_1_dev, Developer)))
# Since "Developer" is a subclass of "Employee" the emp_1_dev is still considered a instance of both classes
print("Is emp_1_dev an instance of the Employee class?: " + str(isinstance(emp_1_dev, Employee)))

print("\n")

print("Is Developer a subclass of Employee?: " + str(issubclass(Developer, Employee)))



