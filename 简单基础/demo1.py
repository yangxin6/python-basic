def fun1():
    print("fun1")


def fun2():
    print("fun2")


def fun3():
    print("fun3")


func_dict = {
    '1': fun1,
    '2': fun2,
    '3': fun3
}

ch = '1'
if ch in func_dict:
    func_dict[ch]()  # 调用 fun1函数
