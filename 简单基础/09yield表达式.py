def eat(name):
    print('[1] %s is ready for eating' % name)
    food_list = []
    while True:
        food = yield  # yield 可以赋值给一个变量
        print('[2] %s starts to eat %s' % (name, food))
        food_list.append(food)
        print('[3] %s has eaten %s' % (name, food_list))


"""
person1 = eat('Albert')

# 函数停在 food = yield 这行代码
person1.__next__()

# 继续执行代码, 由于 yield没有值，即 yield = None, 这 food = None
person1.__next__()
"""

person1 = eat('Albert')
"""
表达式 yield 使用必须初始化
第一次必须传 None， 或者用__next__方法
"""

# person1.send(None)  初始化和 __next__()作用一样
person1.__next__()

person1.send('羊肉')  # send 传值 初始化
person1.send('牛肉')
person1.send('面包')
person1.send('牛奶')
person1.close()  # 关闭之后就不能send了
# person1.send('error')
