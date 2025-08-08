# Mission: To define the fundamental data structures for our system
class Student: 
    def __init__(self, student_id, name):
        self.id = student_id
        self.name = name
        self.enrolled_in = []

class Teacher: 
    def __init__(self, teacher_id, name, speciality): 
        self.id = teacher_id
        self.name = name
        self.speciality = speciality

#Data bases
student_db = []
teacher_db = []
next_student_id = []
next_teacher_id = []
