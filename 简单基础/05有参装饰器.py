import time


current_user = {
    'username': None
}


def auth(engine):
    def user_auth(func):
        def wrapper(*args, **kwargs):
            if engine == 'file':
                print('基于文件的认证')
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
            elif engine == 'mysql':
                print('mysql的认证')
            elif engine == 'ldap':
                print('ldap的认证')
        return wrapper
    return user_auth


@auth('file')
def index():
    time.sleep(1)
    print("welcome to index")
    return 1


@auth('mysql')
def home(name):
    time.sleep(2)
    print("welcome to home %s" % name)


index()
home('Albert')
