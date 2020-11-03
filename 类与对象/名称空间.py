class DeepShareStudent:
    school = 'syau'
    name = 'aaaaaaaa'
    def __init__(self, name, age):
        print("===== init run =====>")
        self.name = name
        self.age = age

    def learn(self):
        print("%s is learning" % self.name)

    def eat(self):
        print("is eating")

    def sleep(self):
        print("is sleeping")

    def choice(self, course):
        print("%s is chosing %s " % (self.name, course))

stu1 = DeepShareStudent("杨", 1)
stu2 = DeepShareStudent("杨2", 2)
print(stu1.__dict__)

# DeepShareStudent.learn('A')
stu1.learn()

print(stu1.learn)
print(stu2.learn)

stu1.learn()
stu2.learn()

stu1.choice("AI")
stu2.choice("Python")

