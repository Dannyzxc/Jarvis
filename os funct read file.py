import os
print('current working directory is:  ' + os.getcwd())
a = open('justtext.txt', 'r')
b = a.read()           # read() prints in string format
print(b)
a.close()

d = open('justtext.txt', 'r')
c = d.readlines()              # readlines() print in list format
print(c)
d.close()
