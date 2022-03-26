import os,zipfile
# reading zip file
print(os.getcwd())
a = os.chdir('C:\\Users\Dnyane\Downloads\\test file')  # changing dir
print(os.getcwd())

for i in os.listdir('C:\\Users\Dnyane\Downloads\\test file'):
    print(i)

# converted folder '3' into newZip.zip
b = zipfile.ZipFile('newZip.zip', 'w')
b.write('3', compress_type=zipfile.ZIP_DEFLATED)
b.close()
