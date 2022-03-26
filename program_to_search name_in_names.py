# program_to_search name_in_names
def searcher():
    import time
    # some four secand time consuming task
    names = 'danny, harry, jonny, penny, jenny, honey'
    time.sleep(4)


    while True:
        text = (yield)
        if text in names:
            print('your name is present')
        else:
            print('your name is not present')


search = searcher()
print('search started')
next(search)
print('next method run')
search.send('danny')
input('press any key')
