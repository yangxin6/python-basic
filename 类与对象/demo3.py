class DeepShareStudent:
    school = 'syau'
    NAME = 'aaaaa'
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


stu1 = DeepShareStudent('张三', 1)
print(stu1.NAME)
print(stu1.school)
stu1.school = "syau1"
print(stu1.school)
DeepShareStudent.school = "syau2"
print(stu1.school)

stu2 = DeepShareStudent('张三2', 2)
print(stu2.NAME)
print(stu2.school)