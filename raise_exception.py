# raise_exception

c= input('enter your name ')
try:
    print(a)

except Exception as e:
    if c == 'danny':
        print('you are not allowed')

    print('Exeption handled')


#or

a = input('name ')
b = input('earning ')
if int(b) == 0:
    raise zeroDivisionError('b= 0 so programmed is stopped')
if a.isnumeric():
    raise Exception('numbers are not allowed')

print(f'hello {a}')