
def outer():
    name = "albert"

    def inner():
        print("inner is %s" % name)

    return inner


f = outer()
f()
