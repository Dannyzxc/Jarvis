# dunder_method_&_operater_overloading

class employe:
    leaves = 12
    _protec = 100
    __privata = 200
    def  print_0(self):
        return f'name is {self.name}.salary is {self.std}'

    def __init__(self,aname,salary,role):
        self.aname= aname
        self.salary = salary
        self.role = role

    def __add__(self, other):               # dunder_method
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f'name is {self.aname}.salaryy is {self.salary}'

    def __str__(self):
        return f'name is {self.aname}.salaryy is {self.salary}'


emp_1 = employe('james', 1000, 'junior')
emp_2 = employe('danny', 2000, 'junior')
print(emp_1.salary)
print(emp_1 + emp_2)
print(emp_1 / emp_2)
print(emp_1)
print(repr(emp_2))




