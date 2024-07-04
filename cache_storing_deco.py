import time
def cache(func):
    cache_value = {}
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper    


@cache
def running_function(a,b,c=10):
    time.sleep(3)
    return a+b+c


print(running_function(1,2))
print(running_function(1,2))
