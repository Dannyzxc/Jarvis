import os
a = os.path.join('usr', 'bin', 'spam')
print(a)
print('--------------')

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('C:\\Users\\asweigart', filename))

print('\n1111111111\n')
# finds current working directory
b = os.getcwd()
print(b)
print('\n22222\n')

# os.chdir('C:\\Windows\\System32')
os.chdir('C:\\Users\Dnyane\Documents\py') # reseting directory
c = os.getcwd()
print('current working directory is:  ' + c)

print('\n3333\n')
# program to create folder
d = os.makedirs('C:\\Users\Dnyane\Documents\py\os_functions')
