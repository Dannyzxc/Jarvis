# program of class methods using split funct and cls eg 3

class Students:
    school0 = 'ABS school'
    def  print_0(self):
        return f'name is {self.name}.salary is {self.std}'

    def __init__(self,aname,time,place):
        self.name = aname
        self.timing = time
        self.location = place

    @classmethod
    def change_school(cls,new_school):
        cls.school0 = new_school

    @classmethod
    def from_dash1(cls, string0):
        saving_1 = string0.split('-')
        return cls(saving_1[0],saving_1[1],saving_1[2])

    # or

    @classmethod
    def from_dash2(cls, string1):
        return cls(*string1.split('-'))



john = Students('john',8,'chips')

john.change_school('goa_university')
print(john.school0)

karan = Students.from_dash1('karan-9-table')
print(karan.timing)

varan = Students.from_dash2('varan-10-spoon')
print(varan.timing)