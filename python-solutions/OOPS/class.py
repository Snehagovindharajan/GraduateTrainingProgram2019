# class Student:
#     age=21
#     def student_report():
#         print("Yes")
# s = Student()
# s.student_report()
# # Student.student_report()

# def A():
#     a=12
# def B():
#     b= a + 1
#     print(b)
# A()
# B()

class Student:
    def __init__(self,name):
        self.name = name
    def display(self):
        self.name = "Miss "+self.name
        print(self.name)


s = Student("Sneha")
s.display()