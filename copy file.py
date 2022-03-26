import os ,shutil
print(os.getcwd())

# to copy from source to destination
os.chdir('C:\\')
# the original spam.txt filename is used for the new, copied file’s filename. The second shutil.
shutil.copy('C:\\Users\Dnyane\Documents\py\main4.py','C:\\Users\Dnyane\Documents\py\os funct 2')

# copy() call also copies the file at C:\\Users\Dnyane\Documents\py\main4.py to the folder
# C:\\Users\Dnyane\Documents\py\os funct 2 but gives the copied file the name main6.py

shutil.copy('C:\\Users\Dnyane\Documents\py\main4.py','C:\\Users\Dnyane\Documents\py\os funct 2\main6.py')

# While shutil.copy() will copy a single file, shutil.copytree() will copy an entire folder and every folder and
# file contained in it. Calling shutil.copytree(source, destination) will copy the folder at the path source,
# along with all of its files and sub-folders, to the folder at the path destination.
# The source and destination parameters are both strings.The function returns a string of the path of the copied folder

shutil.copytree('C:\\Users\Dnyane\Documents\Bandicam','C:\\Users\Dnyane\Downloads\Bcam')
