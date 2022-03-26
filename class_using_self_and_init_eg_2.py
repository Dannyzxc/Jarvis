# program of class eg 2 using self and init and static class

class Students:
    school0 = 'ABS school'
    def  print_0(self):
        return f'name is {self.name}.salary is {self.std}'

danny = Students()
danny.name = 'danny'
danny.std = 12
danny.subjects = ['physics', 'chem', 'maths']

print(danny.print_0())

class employe:
    def __init__(self,breakfast,time,place):
        self.eat = breakfast
        self.timing = time
        self.location = place

    @classmethod
    def printing_good(ab):
        print('this is good' + ab)


james = employe('bread', 11 , 'kitchen')
print(james.eat)

print('--------------------')
employe.printing_good('dan')