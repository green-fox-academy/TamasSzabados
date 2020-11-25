class Teacher:
    def __init__(self, name):
        self.name = name

    def answer(self):
        print("the teacher is answering a question")

    def teach(self,student):
        return student.learn()