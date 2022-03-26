import time

def lots_of_num(max):
    for x in range(0,max):
        print(x)




def lots_of_num(max):
    t1 = time.time()
    for x in range(0,max):
        print(x)
    t2 = time.time()
    print('it took %s seconds ' %(t2-t1))

    
lots_of_num(200)