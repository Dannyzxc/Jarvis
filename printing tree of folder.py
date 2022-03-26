import os

print(os.getcwd())
# printing entire tree of a folder
for folderName, subfolders, filenames in os.walk('C:\\Users\Dnyane\Downloads\\test file'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

        for filename in filenames:
            print('FILE INSIDE ' + folderName + ': ' + filename)
        print('')