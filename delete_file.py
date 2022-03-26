import os,shutil, send2trash

# print(os.getcwd())

a = os.listdir('C:\\Users\Dnyane\Downloads')
# print(a)
b = os.listdir('c:\\Users\Dnyane\Downloads\\test file')
print(b)
print('---------')
# both ways below did't work
for filename1 in b:
    if filename1.endswith('.png'):
        shutil.rmtree(filename1)
        # print(filename)

for filename2 in b:
    if filename2.endswith('.png'):
        os.unlink(filename2)
        # print(filename)

# another way to delete file
baconFile = open('bacon.txt', 'a') # creates the file
baconFile.write('Bacon is not a vegetable.')

baconFile.close()
send2trash.send2trash('bacon.txt')
