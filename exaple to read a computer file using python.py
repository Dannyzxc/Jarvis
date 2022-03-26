test_file = open('/home/danny/test_01.txt','w')
test_file.write('i wrote this text using python commands')
test_file.close()

test_file = open('/home/danny/test_01.txt')
text = test_file.read()
print(text)
