import os,zipfile
# reading zip file
print(os.getcwd())
os.chdir('C:\\Users\Dnyane\Downloads\\test file')  # changing dir
print(os.getcwd())
zip1 = zipfile.ZipFile('cats.zip')               # passing file
a = zip1.namelist()
print(a)

zip1.extractall()
zip1.close()
# extracted single file from the the zip folder
zip1.extract('1/catnames.txt')