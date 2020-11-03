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


@auth
def index():
    time.sleep(1)
    print("welcome to index")
    return 1


@auth
def home(name):
    time.sleep(2)
    print("welcome to home %s" % name)


index()
home('Albert')
