class Student:

    def __init__(self, name, dept, cgpa, current_semester):
        self.name = name
        self.dept = dept
        self.cgpa = cgpa
        self.current_semester = current_semester

    def is_honor_roll(self):
        if self.cgpa >= 3.5:
            return True
        else:
            return False

