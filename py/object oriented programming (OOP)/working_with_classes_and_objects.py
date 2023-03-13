# object oriented programming in python
class Student:
    def __init__(self, name, age, grade) -> None:
        self.name = name
        self. age = age
        self. grade = grade #0-100

    def get_grade(self):
        return self.grade     

class Course:
    def __init__(self, name, max_stidents) -> None:
        self.name = name
        self.max_students = max_stidents
        self.students = []    

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value/len(self.students)             

stud_1 = Student("Collins", 19, 95)
stud_2 = Student("Alex", 19, 75)
stud_3 = Student ("Marco", 19, 65)

Course = Course ("Science", 2)
Course.add_student(stud_1)
Course.add_student(stud_2)
print(Course.get_average_grade())