class DeepSharePeople:
    school = 'syau'
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def f1(self):
        print('father f1')


class DeepShareTeacher(DeepSharePeople):
    def modify_score(self):
        print('teacher %s is modifying score' % self.name)

    def f1(self):
        print('son f1')

teal = DeepShareTeacher('Albert', 16, 'male')
teal.f1()