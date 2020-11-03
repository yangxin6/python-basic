class DeepSharePeople:
    school = 'syau'
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def f1(self):
        print('father f1')
    def info(self):
        print("""
        ========= personal info =========
        name: %s
        age: %s
        gender: %s
        """ % (self.name, self.age, self.gender))

class DeepShareTeacher(DeepSharePeople):
    def __init__(self, name, age, gender, level, salary):
        super().__init__(name, age, gender)
        # self.name = name
        # self.age = age
        # self.gender = gender
        self.level = level
        self.salary = salary
    def modify_score(self):
        print('teacher %s is modifying score' % self.name)

    def f1(self):
        print('son f1')

    def info(self):
        super().info()
        print("""
        ========= personal info =========
        level: %s
        salary: %s
        """ % (self.level, self.salary))

teal = DeepShareTeacher('Albert', 16, 'male', 10, '3333')
teal.info()