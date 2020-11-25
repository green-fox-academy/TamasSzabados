class Student:
    def __init__(self, name):
        self.name = name

    def learn(self):
        print("the student is learning something new")

    def question(self,teacher):
        return teacher.answer()