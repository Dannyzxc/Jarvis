# function_caching_and_time_delay
import time
from functools import lru_cache

@lru_cache(maxsize=3)
def some_work(t):
    time.sleep(t)
    return t

if __name__ == '__main__':
    print('now running some work')
    some_work(3)
    print('done calling again')
    some_work(3)
    print('called again')
