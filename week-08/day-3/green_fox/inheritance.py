class Person():
    def __init__(self, name = "Jane Doe", age = 30, gender= "female"):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print("Hi, I'm " + self.name + ", a " + str(self.age) + " year old " + self.gender +".")
    
    def get_goal(self):
        print("My goal is: Live for the moment!")

class Student(Person):
    def __init__(self, name = "Jane Doe", age = 30, gender= "female", previous_organization = "The School of Life"):
        super().__init__(name, age, gender)
        self.previous_organization = previous_organization
        self.skipped_days = 0

    def get_goal(self):
        print("Be a junior software developer.")

    def introduce(self):
        print("Hi, I'm "+ self.name + ", a " + str(self.age) + " year old " + self.gender +" from "+ self.previous_organization + "who skipped " + str(self.skipped_days) + "days from the course already.")

    def skip_days(self, number_of_days):
        self.skipped_days += number_of_days
        return self.skipped_days

class Mentor(Person):
    def __init__(self, name = "Jane Doe", age = 30, gender= "female", level ="intermediate" ):
        super().__init__( name, age, gender)
        self.level = level

    def get_goal(self):
        print("Educate brilliant junior software developers")

    def introduce(self):
        print("Hi, I'm "+ self.name + ", a " + str(self.age) + " year old " + self.gender +" " + self.level + "mentor.")


class Sponsor(Person):
    def __init__(self, name = "Jane Doe", age = 30, gender= "female", company = "Google"):
        super().__init__(name, age, gender)
        self.company = company
        self.hired_students = 0

    def get_goal(self):
        print("Hire brilliant junior software developers.")

    def introduce(self):
        print("Hi, I'm "+ self.name + ", a " + str(self.age) +" year old " + self.gender +" who represents " + self.company + " and hired" + str(self.hired_students) + " students so far.")

    def hire(self):
        self.hired_students += 1
        
class Cohort():
    def __init__(self, name,):
        self.name = name
        self.students = []
        self.mentors =[]

    def add_student(self, student):
        self.students.append(student)
        return self.students

    def add_mentor(self, mentor):
        self.mentors.append(mentor)
        return self.mentors

    def info(self):
        print("The " + self.name + " cohort has " + str(len(self.students)) + " students and " + str(len(self.mentors)) + " mentors.")



        


