import os
# 'w' will start from scratch
# 'a' append will continue after

a = open('justtext.txt', 'w')
b = a.write('yes i am okay')
a.close()

d = open('justtext.txt')
c = d.read()
print(c)
d.close()
print('------')
e = open('justtext.txt', 'a')
e.write('\ngood to hear')
e.close()

f = open('justtext.txt')
g = f.read()
print(g)
f.close()