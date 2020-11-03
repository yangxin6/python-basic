import time


current_user = {
    'username': None
}


def auth(func):
    def wrapper(*args, **kwargs):
        if current_user['username']:
            print('已登录')
            res = func(*args, **kwargs)
            return res

        name = input('用户名>>：').strip()
        pwd = input('密码>>：').strip()
        if name == 'Albert' and pwd == '1':
            print('登录成功')
            current_user['username'] = name
            res = func(*args, **kwargs)
            return res
        else:
            print('用户名或密码错误')

    return wrapper


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        stop_time = time.time()
        print(stop_time - start_time)
        return res

    return wrapper


# timer 统计 auth + index 的执行时间
@timer
@auth
def index():
    time.sleep(1)
    print("welcome to index")
    return 1


# timer 统计 index 的执行时间
@auth
@timer
def home(name):
    time.sleep(2)
    print("welcome to home %s" % name)


index()
home('Albert')
