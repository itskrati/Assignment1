class Student :
    def __init__ (self, name , RollNumber, Course, Age):
        self.name = name
        self.RollNumber = RollNumber
        self.Course = Course
        self.Age = Age

student1 = Student(name="Krati", RollNumber = 1, Course="Computer Science", Age = 21)
student2 = Student(name="Kartik", RollNumber = 2, Course = "Machine Learning", Age = 22)
student3 = Student(name="Aditi", RollNumber = 3, Course = "Artificial Intelligence", Age = 21)

def display(student):
    print(f"Name: {student.name}")
    print(f"RollNumber: {student.RollNumber}")
    print(f"Course: {student.Course}")
    print(f"Age: {student.Age}")
    print()
print("Student 1:")
display(student1)

print("Student 2:")
display(student2)

print("Student 3:")
display(student3)
    
