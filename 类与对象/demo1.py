# 对象用法
# 定义类 ==> 调用类 ==> 产生对象

class DeepShareStudent:
    school = 'syau'
    print("========>")

    def __init__(self, name, age):
        print("===== init run =====>")
        self.NAME = name
        self.AGE = age

    def learn(self):
        print("%s is learning" % self)

    def eat(self):
        print("is eating")

    def sleep(self):
        print("is sleeping")


stu1 = DeepShareStudent('战士', 14)

print(stu1.NAME)
print(stu1.AGE)
print(stu1.school)
print(stu1.learn)
