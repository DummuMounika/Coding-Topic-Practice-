class Employee:
    #variables
    raise_amount = 1.25
    no_of_emp = 0
    def __init__(self, first, last, pay):
        self.first= first
        self.last=last
        self.pay=pay
        self.email= first + '' + last + '@company.com'

        Employee.no_of_emp += 1
    #method
    #self must be arugment to use the variables
    def fullname(self):
       return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

print(Employee.no_of_emp)
#instance created
emp_1 = Employee('Mounika','Dummu',500000)
emp_2 = Employee('Venu','Dummu',700000)
print(Employee.no_of_emp)
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# emp_1.raise_amount=1.50
# print(emp_1.__dict__)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)