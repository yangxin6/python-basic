import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        stop_time = time.time()
        print(stop_time - start_time)
        return res

    return wrapper


@timer
def index():
    time.sleep(1)
    print("index")
    return 1


# @timer
def home(name):
    time.sleep(2)
    print("home %s" % name)


index()
home("albert")
