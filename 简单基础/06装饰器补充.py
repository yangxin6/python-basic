from functools import wraps


def deco(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@deco
def index():
    """哈哈哈"""
    print(index.__doc__)


index()