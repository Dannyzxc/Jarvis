import shelve
shelfFile = shelve.open('myshelveFile')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats # saving data in shelvefile like dictionary
shelfFile.close()

shelfFile = shelve.open('myshelveFile')
print(shelfFile['cats'])     # getting shelves data which is encoded
shelfFile.close()

shelfFile = shelve.open('myshelveFile')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()

