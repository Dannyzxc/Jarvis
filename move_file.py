import os , shutil

print(os.getcwd())
# move file from source to destination and rename it from manin4.py to move_file.py
shutil.move('C:\\Users\Dnyane\Documents\py\os funct 2\main4.py','C:\\Users\Dnyane\Documents\py\os funct 2\move_file.py')

# renaming file in the same directory
shutil.move('C:\\Users\Dnyane\Documents\py\os funct 2\main5.py','C:\\Users\Dnyane\Documents\py\os funct 2\delete_file.py')

