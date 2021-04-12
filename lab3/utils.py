import time,timeit
def profile(func):
    def wrapper(*args, **kw):
        local_time = timeit.default_timer()
        data  =func(*args, **kw)
        print('time is :',timeit.default_timer() - local_time)
        print(data)
    return wrapper



class timer():
    def __enter__(self):
        self.starttime = timeit.default_timer()

    def __exit__(self, type, value, trace):
        print("time is :", timeit.default_timer() - self.starttime)

if __name__ == '__main__':

    @profile
    def some_function():
        return sum(range(1000))
    result = some_function()  #

    with timer():
        print(sum(range(1000)))
