# library_project

class library:

    def new_book(self):
        e = int(input('enter how many items you wish to enter: '))
        shelfs = {}
        for k in range(0, e):
            l = input('enter author: ')
            m = input('enter Book name: ')
            shelfs[l] = m

    def donate(self):
        f = int(input('enter how many items you wish to donate: '))
        shelfs = {}
        for k in range(0, f):
            l = input('enter author: ')
            m = input('enter Book name: ')
            shelfs[l] = m

    def lend(self):
        pass
    def return_book(self):
       pass
    def display(self):
       print(shelfs)

