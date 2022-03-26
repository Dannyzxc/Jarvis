# program protected and private of class eg 2 using self and init

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



james = employe('james',1000,'junior')
print(james.salary)

emp = employe('danny',2000,'senior')
print(emp._protec)                          # accessing protected part
print(emp._employe__privata)                # accessing private part


