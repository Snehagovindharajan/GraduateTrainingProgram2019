# private only within the class
class Employee:
    def __init__(self, name,age):
        self.name = name
        self.__age = age

    def display_detail(self):
        print("Name : ", self.name,  "Age : ", self.__age)


class Permanent_Employee(Employee):
    def __init__(self, name, salary, age):
        super().__init__(name, age)
        self.salary = salary

    def display_details(self):
        # print("Salary : ", self.salary, "Age : ", self.__age)
        print("Salary : ", self.salary)


per_emp = Permanent_Employee('sneha', 10000, 21)
per_emp.display_details()
per_emp.display_detail()

# private o/p
# When __age is print within the class then age will print. when accessed from other class will print error
# Traceback (most recent call last):
#   File "C:/Users/A08019dirp_c2e.03.06/PycharmProjects/dayone/OOPS/access-modifiers.py", line 17, in <module>
#     per_emp.display_details()
#   File "C:/Users/A08019dirp_c2e.03.06/PycharmProjects/dayone/OOPS/access-modifiers.py", line 13, in display_details
#     print("Name : ", self.name, "Salary : ", self.salary, "Age : ",self.__age)
# AttributeError: 'Permanent_Employee' object has no attribute '_Permanent_Employee__age'
