# Python OOP Tutorial 2: Class Variables - https://www.youtube.com/watch?v=BJ-VvGyQxho

# this program explaine class variables

# Python OOP 1 - Classes and Instances - https://youtu.be/ZDa-Z5JzLYM
# Python OOP 2 - Class Variables - https://youtu.be/BJ-VvGyQxho
# Python OOP 3 - Classmethods and Staticmethods - https://youtu.be/rq8cL2XMM5M
# Python OOP 4 - Inheritance - https://youtu.be/RSl87lqOXDE
# Python OOP 5 - Special (Magic/Dunder) Methods - https://youtu.be/3ohzBxoFHAY
# Python OOP 6 - Property Decorators - https://youtu.be/jCzT9XFZ5bw

class Employee:

    raise_amount = 1.04 #class variable. this variable must be accessed via self or Employee
    number_of_emps = 0 # also class variable. but accessing via self will not make sense.

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.number_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print('Number of employees:', Employee.number_of_emps)

print(emp_1.__dict__)
print()
#print(Employee.__dict__)
print('Corey - before raise:', emp_1.pay)
emp_1.apply_raise()
print('Corey - new pay:', emp_1.pay)

print('Test - before raise:', emp_2.pay)
emp_2.apply_raise()
print('Test - new pay:', emp_2.pay)