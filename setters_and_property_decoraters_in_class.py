# setters_and_property_decoraters_in_class

class employe:
    def __init__(self,fname,lname):
        self.fname= fname
        self.lname = lname
        self.email = f'{fname}.{lname}@jerry.com'

    def explain(self):
        return f'this employee is {fname} {lname}'

    def print_email(self):
        pass


emp1 = employe('danny','g')
emp2 = employe('jerry','white')

print(emp1.email)
emp1.fname = 'manny'
print(emp1.email)
print('------------------------------------')

# name did not change so we put setters

class employe2:
    def __init__(self,fname2,lname2):
        self.fname2= fname2
        self.lname2 = lname2


    def explain(self):
        return f'this employee is {fname2} {lname2}'

    def emails(self):
        return f'{self.fname2}.{self.lname2}@jerry.com'


emp3 = employe2('danny','g')
emp4 = employe2('jerry','white')

print(emp3.emails())
emp3.fname2 = 'gandhi'
print(emp3.emails())
print('------------------------------------')

# same thing but using property decoraters

class employe2:
    def __init__(self,fname3,lname3):
        self.fname3= fname3
        self.lname3 = lname3


    def explain(self):
        return f'this employee is {fname3} {lname3}'

    @property
    def emails(self):
        return f'{self.fname3}.{self.lname3}@jerry.com'


emp5 = employe2('danny','g')
emp6 = employe2('jerry','white')

print(emp5.emails)                  # not assigned as functions
emp5.fname3 = 'gandhi'
print(emp5 .emails)
print('------------------------------------')
