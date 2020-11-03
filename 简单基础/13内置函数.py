res = '{} {} {}'.format('Albert', 18, 'male')  # 相当于 %
print(res)

res = '{1} {0} {1}'.format('Albert', 18, 'male')  # 根据索引对应值
print(res)

res = '{name} {age} {sex}'.format(sex='male', name='Albert', age=20)
print(res)


class Person(object):
    # 相当于构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 相当于 toString
    def __str__(self):
        return "This guy is {self.name}, {self.age} years old.".format(self=self)


p1 = Person("Albert", 18)
print(p1)

c = (250, 250)
# s1 = "敌人坐标：%s" % c   # error
s1 = "敌人坐标：{}".format(c)
print(s1)

name = 'Albert'
print(f'he said his name is {name}')

print('{:>10}'.format('18'))
print('{:3<10}'.format('18'))
print('{:*^10}'.format('18'))
print('a'.zfill(10))  # 右对齐 填充0 指定长度为10

print('{:.4f}'.format(3.1415926535))  # 4位小数 精度为5 四舍五入

print('{:b}'.format(18))  # 二进制
print('{:d}'.format(18))  # 十进制
print('{:o}'.format(18))  # 八进制
print('{:x}'.format(18))  # 十六进制

print(bin(18))
print(oct(18))
print(hex(18))

print(abs(-1))

print(all([1, 'a', True]))  # True
print(all([1, 'a', True, 0]))  # False
print(any([1, 'a', True, None, False]))  # True
print(any([1, 'a', True]))  # True
print(any([]))  # False
print('---------------------')
print(bool(0))  # False
print(bool(1))  # True
print(bool('a'))  # True
print(bool(''))  # True

print('=========================')

# bytes 类型构造
res = '你好Albert'.encode('utf-8')  # unicode 按照 utf-8 进行编码，得到的结果为 bytes 类型
print(res)

res = bytes('你好Albert', encoding='utf-8')
print(res)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')


def func():
    pass


# 判断对象是否可调用
print(callable(func))
print(callable('abc'.strip))
print(callable(max))

print('1~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# 字符与十进制转换
print(chr(65))  # 按照 ascii 码表 将十进制数转为字符
print(ord('a'))  # 按照 ascii 码表 将字符转为十进制数

# 查看对象下可调用的方法
print(dir('abc'))

# 去商和余数返回元组
print(divmod(1331, 25))

# 将字符内的表达式拿出运行，得到表达式的执行结果
res1 = eval('2*3')
print(res1, type(res1))
res2 = eval('[1,3,5]')
print(res2, type(res2))
res3 = eval('{"name":"Albert", "age":18}')
print(res3, type(res3))

s = {1, 3, 4}
s.add(5)
print(s)
f_set = frozenset(s)
print(f_set, type(f_set))

x = 2
print(globals())
print(dir(globals()['__name__']))

print(hash('a'))
print(hash((1, 3, 5, 7, 9)))


def func1():
    """
    注释
    :return:
    """
    pass


print(help(max))
print(help(func1))

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# 2 ** 3 % 3
print(2 ** 3 % 3)
print(pow(2, 3, 3))

i = [1, 4, 7, 2]
res = reversed(i)
print(list(res))
print(i)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# [start_index : end_index : step]
sc = slice(1, 5, 2)
l = ['a', 'b', 'c', 'd', 'e', 'f']
print(sc)
print(l[1:5:2])
print(l[sc])

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')

left = 'hello'
right1 = {'x': 1, 'y': 2, 'z': 3}
right2 = [1, 3, 5, 7, 9]
res1 = zip(left, right1)
res2 = zip(left, right2)
print(list(res1))
print(list(res2))

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')

a = [1, 2, 3]
b = [4, 5, 6]
zipAB = zip(a, b)
print(list(zipAB))
for i in zip(*zipAB):
    print(i)
nums = ['123', '456', '789']
print(nums)
for j in zip(*nums):
    print(j)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')

l1 = ['egg%s' % i for i in range(10)]
l2 = ['egg%s' % i for i in range(10) if 2 < i < 7]
print(l1)
print(l2)
l3 = ('egg%s' % i for i in range(10))
print(next(l3))
print(next(l3))
