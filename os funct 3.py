import os

b = os.getcwd()   # getting file
print('current working directory is:  ' + b)
a = os.path.getsize(b)   # getting size of file specified
print(a)
c = os.listdir(b)     # lists of files
print(c)

all_files = os.listdir('C:\\Users\\Dnyane\\Documents\\py')    # lists of files
print(all_files)

print('-----------')
# getiing total size of all the paths
totalSize = 0
for files in all_files:
    folderPaths = ('C:\\Users\\Dnyane\\Documents\\py')
    totalSize = totalSize + os.path.getsize(os.path.join(folderPaths, files))
print(totalSize)

