import time
import os
from memory_profiler import profile

def timing(f):
    def wrap(*args, **kwargs):
        start_time = time.monotonic()
        result = f(*args, **kwargs)
        end_time = time.monotonic()
        print(f'{f.__name__} function took {(end_time - start_time) * 1000.0} ms')
        return result
    return wrap

@profile
@timing
def test():
    for i in range(1000000):
        print(i**2)

if __name__ == '__main__':
    test()

