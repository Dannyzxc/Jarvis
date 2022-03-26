# coroutines_in_python_with_searcher
def searcher():
    import time
    # some four secand time consuming task
    book = 'this is a book containing lots of documents and used for some python program'
    time.sleep(4)


    while True:
        text = (yield)
        if text in book:
            print('your text is in the book')
        else:
            print('this is not in the book')


search = searcher()
print('search started')
next(search)
print('next method run')
search.send('this')
input('press any key')
