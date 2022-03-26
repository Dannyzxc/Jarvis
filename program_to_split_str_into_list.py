
#program to split str into list
def from_str(a):
    saving_1 = a.split(' ')
    return saving_1[0], saving_1[1], saving_1[2]

b = 'hello im danny'
print(from_str(b))
