# Python OOP Tutorial 1: Classes and Instances - https://www.youtube.com/watch?v=ZDa-Z5JzLYM

# This program explains Classes and Instances.
# Instance variables contain Data that is unique to each instance

# Python OOP 1 - Classes and Instances - https://youtu.be/ZDa-Z5JzLYM
# Python OOP 2 - Class Variables - https://youtu.be/BJ-VvGyQxho
# Python OOP 3 - Classmethods and Staticmethods - https://youtu.be/rq8cL2XMM5M
# Python OOP 4 - Inheritance - https://youtu.be/RSl87lqOXDE
# Python OOP 5 - Special (Magic/Dunder) Methods - https://youtu.be/3ohzBxoFHAY
# Python OOP 6 - Property Decorators - https://youtu.be/jCzT9XFZ5bw

class Employee:
    def __init__(self, first, last, pay):
        self.first = first                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corry', 'Schafer', 50000) # instace variable
emp_2 = Employee('Test', 'User', 60000) # instance variable

#print(emp_1)
#print(emp_2)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname()) #instance variable already declared, hence fulname() doesn't need to get parameter.
print(Employee.fullname(emp_1)) # using class directly, since there is no instance of Employee, emp_1 must be passed. this is where self parameter is received.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 