list_1 = []
with open('words.txt') as f:
    lines = f.readlines()
    word = [x.strip() for x in lines]
    list_1.append(word)

print(list_1)

with open('words_02.py', 'a') as j:
    j.write(str(list_1))

# with open('words.txt', 'a') as f:
    # lines = f.readlines()
    # word = [x.strip() for x in lines]
    # lines2 = [line.rstrip() for line in f]


# print(word)
# print(lines2)