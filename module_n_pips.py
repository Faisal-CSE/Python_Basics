#From student file import Student class
from student import Student

student1 = Student("Porag", "CSE", 3.77, 4)

student2 = Student("Faisal", "EEE", 3.57, 7)

print("Student name: "+student1.name)
print("Department: "+student1.dept)
print("Current CGPA: "+str(student1.cgpa))
print("Current Semester: "+str(student1.current_semester))

print("--------------------------")

print(student2.cgpa)
