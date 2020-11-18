class Employee:
    # __init__ automatically initiates an instance. This way we don't have to define each variable manually for
    # each instance of a class
    def __init__(self, first_name, last_name, pay):
        # "self" refers to the instance. Like saying emp_1/emp_2.first_name = first_name
        # Instance variables. Unique to each instance of this class
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + "." + last_name + "@company.com"

    # Class method/function
    def fullname(self):  # Really important to remember to insert the "self"
        return '{} {}'.format(self.first_name, self.last_name)


# We create an "instance" of a class by calling it. Each class instance is unique.
# We pass in the first_name, last_name and the pay. The "self" reference is passed automatically
emp_1 = Employee('Rasmus', 'Thomsen', 30000)
emp_2 = Employee('Danny', 'Devito', 1000000)
print("Name: {}\n" "Last Name: {}\n" "Pay: {}\n".format(emp_1.first_name, emp_1.last_name, emp_1.pay))
print("Name: {}\n" "Last Name: {}\n" "Pay: {}\n".format(emp_2.first_name, emp_2.last_name, emp_2.pay))

# Calling a class method. Remember the '()'. Here the "self" is again passed automatically
print("Full Name: " + emp_1.fullname())

# Does exactly the same as above. We call the same method through the Class. This time we have to pass the
# instance as an argument
print("Full Name: " + Employee.fullname(emp_2))
