# 为 index 函数添加一个统计时间的功能
import time


def index():
    time.sleep(1)
    print("index")
    return 1


def home(name):
    time.sleep(2)
    print("home %s" % name)


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        stop_time = time.time()
        print(stop_time - start_time)
        return res

    return wrapper


index = timer(index)  # 新的 index = wrapper
home = timer(home)

home(name='Albert1')
home('Albert2')
index()


# 修饰器模板
def outer(func):
    def inner(*args, **kwargs):
        """
        写装饰器的逻辑
        :param args: 任意位置参数
        :param kwargs: 任意关键参数
        :return: 一个函数对象
        """
        res = func(*args, **kwargs)
        return res

    return inner
