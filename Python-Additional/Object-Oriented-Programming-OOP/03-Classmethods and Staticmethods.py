class Employee:
    # Class variables/attributes. Shared by all instances of a class
    num_of_employees = 0
    raise_amount = 1.05

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + "." + last_name + "@company.com"

        Employee.num_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod  # This is called a decorator. Specifies the function of the following method
    # As can be seen the class is the first argument instead of the instance
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # Using a class method as an alternative constructor
    @classmethod
    # Takes in a string, splits it and creates an instance to return
    def from_string(cls, emp_string):
        first_name, last_name, pay = emp_string.split('-')
        return cls(first_name, last_name, pay)  # This creates a new instance/object by calling the class and returns it

    @staticmethod
    # A staticmethod takes neither the class nor the instance as the first argument. It's essentially a regular function
    def name_backwards(name):  # Just takes in a name as a argument and returns it backwards
        name_list = [letters for letters in name]
        name_list.reverse()
        name = ""
        for letters in name_list:
            name += letters
        return name


emp_1_string = 'Rasmus-Thomsen-30000'
emp_2_string = 'Danny-Devito-1000000'

# Calls the classmethod that splits the string and returns an instance/object
emp_1 = Employee.from_string(emp_1_string)
emp_2 = Employee.from_string(emp_2_string)

print("Class raise amount: ", Employee.raise_amount)
print(emp_1.first_name + "'s " + "pay: ", emp_1.pay)
print(emp_2.first_name + "'s " + "pay: ", emp_2.pay)

print("\n")

# Calling the staticmethod and getting the reversed name
name = "rasmus"
print(name + " backwards is: ", Employee.name_backwards(name))







