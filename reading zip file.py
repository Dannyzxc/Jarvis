import os,zipfile

# reading zip file
print(os.getcwd())
os.chdir('C:\\Users\Dnyane\Downloads\\test file')  # changing dir
print(os.getcwd())
zip1 = zipfile.ZipFile('cats.zip')               # passing file
a = zip1.namelist()
print(a)

print('------------')

# getting file size inside zipfile
for i in a:
    print(i)
    file_info = zip1.getinfo(i)
    print('file size is:')
    print(file_info.file_size)
    print('compressed size is:')
    print(file_info.compress_size)
    if file_info.compress_size != 0:
        print('compress file is %sx smaller' %(round(file_info.file_size / file_info.compress_size, 2)))
    else:
        print('no difference or empty file')
