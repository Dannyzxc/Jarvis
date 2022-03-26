import os
a = os.path.abspath('..')
print(a)
# b = os.path.abspath('.\\Scripts')
b = os.path.abspath('.os_functions')
print(b)
c = os.path.isabs('..')
print(c)
d = os.path.isabs(os.path.abspath('..'))
print(d)
print('\n--------\n')

e = os.path.relpath('C:\\Windows', 'C:\\')
print(e)

f = os.path.relpath('C:\\Windows', 'C:\\spam\\eggs')
print(f)

g = os.getcwd()
print('current working directory is:  ' + g)