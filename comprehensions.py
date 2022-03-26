# list comprehensions
ls = []
for i in range(1, 100):
    if i % 3 == 0:
        ls.append(i)

print(type(ls))
print(ls)
print('-------------------1')

ls0 = [i for i in range(1, 200) if i % 5 == 0]
print(ls0)
print('-------------------2')

# dic
dic_1 = {0: 'item0', 1: 'item1'}
print(dic_1)
print('-------------------3')

# dic comprehensions
dic_2 = {i: f'item{i}' for i in range(1, 300) if i % 10 == 0}
print(dic_2)
print('-------------------4')

# reverse key and value

dic_3 = {value: key for key, value in dic_2.items()}
print(dic_3)
print('-------------------5')

# set comprehensions
dresses = {dress for dress in ['dress1','dress2']}
print(dresses)
print('-------------------6')

# generator comprehension
evens = (i for i in range(1,21) if i % 2 == 0)
print(type(evens))
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())
print('-------------------7')
# or

for items in evens:
    print(items)