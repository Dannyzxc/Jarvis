# program of class eg 1

class Students:
    school0 = 'ABS school'

danny = Students()
danny.name = 'danny'
danny.std = 12
danny.subjects = ['physics', 'chem', 'maths']

print(danny.std, '\n', danny.subjects)
print(danny.school0)
Students.school0 = 'bombay school'
print(Students.school0)

john = Students()
john.name = 'john'
john.std = 12
john.subjects = ['physics', 'chem', 'bio']


print('--------------------1')
john.school0 = 'madras school'
print(danny.school0)
print(john.school0)

print('--------------------2')
print(danny.__dict__)
print(john.__dict__)
print(Students.__dict__)

