class People:
    school = 'syau'

    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(People):
    def learn(self):
        print("%s is learning" % self.name)

class Teacher(People):
    def modify(self):
        print("%s is modifying" % self.name)


stu1 = Student("张三", 18)
tea1 = Teacher("li", 33)
stu1.learn()
tea1.modify()

# 属性查找 方法 命名空间 就近原则
# 对象自己的名称空间 ===> 对象所在的类的名称空间 ===> 对象的所在的类的父类的名称空间
