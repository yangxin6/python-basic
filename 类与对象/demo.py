class DeepShareStudent:
    school = 'syau'

    def learn(self):
        print("%s is learning" % self)

    def eat(self):
        print("is eating")

    def sleep(self):
        print("is sleeping")

    print("========>")


# 使用类型 .__dict__ 方法可以查看 类中的变量和函数
name_and_func = DeepShareStudent.__dict__
print(name_and_func)

print(name_and_func['school'])
print(name_and_func['learn'])

name_and_func['learn']('yang')

print(DeepShareStudent.school)
print(DeepShareStudent.learn)
print(DeepShareStudent.eat)


print("~~~~~~~~~~~~~~~")
DeepShareStudent.school = 'syau1'
print(DeepShareStudent.school)

DeepShareStudent.country = 'China'
print(DeepShareStudent.country)


# 对象用法
# 定义类 ==> 调用类 ==> 产生对象

print("\n==================")
DeepShareStudent()

stu1 = DeepShareStudent()
stu2 = DeepShareStudent()
stu3 = DeepShareStudent()
print(stu1)
print(stu2)
print(stu3)