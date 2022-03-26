# program to enter items in list & dictionary

e = int(input('enter how many items you wish to enter in list: '))
type0 = input('how you want to enter in LIST(l), DICTIONARY(d) or in SET(s): ')
if type0 == 'l':
    ls = []
    for i in range(0,e):
        j = input('enter items: ')
        ls.append(j)

    print(ls)

elif type0 == 'd':
    dict_0 = {}
    for k in range(0, e):
        l = input('enter key: ')
        m = input('enter value: ')
        dict_0[l] = m

    print(dict_0)

elif type0 == 's':
    set0 = set()
    print(type(set0))
    for i in range(0,e):
        j = int(input('enter items: '))
        set0.add(j)

    print(set0)

