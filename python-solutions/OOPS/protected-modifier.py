# protected one level below
class Employee:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def display_detail(self):
        print("Name : ", self.name, "Age : ", self._age)


class Permanent_Employee(Employee):
    def __init__(self, name, salary, age):
        super().__init__(name, age)
        self.salary = salary

    def display_details(self):
        print("Name : ", self.name, "Salary : ", self.salary, "Age : ", self._age)


class Manager(Permanent_Employee):
    def __init__(self, name, salary, age):
        super().__init__(name, salary, age)

    # def display_det(self):
    #     print("Name : ", self.name, "Salary : ", self.salary, "Age : ", self._age)


# per_emp = Permanent_Employee('sneha', 10000, 21)
# per_emp = Employee('sneha',21)
per_emp = Manager('sneha', 10000, 21)
per_emp.display_details()
per_emp.display_detail()
# per_emp.display_det()
per_emp._age
# protected o/p
# Name :  sneha Salary :  10000 Age :  21
#
# Process finished with exit code 0
