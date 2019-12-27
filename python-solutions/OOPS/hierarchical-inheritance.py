class Employee:
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept

    def display_details(self):
        print("Name :", self.name, "Dept :", self.dept,end=' ')


class Permanent_Employee(Employee):
    def __init__(self, name, dept, salary):
        super().__init__(name, dept)
        self.salary = salary

    def display_details(self):
        super().display_details()
        print("Salary :", self.salary)


class Temporary_Employee(Employee):
    def __init__(self, name, dept, salary):
        super().__init__(name, dept)
        self.salary = salary

    def display_details(self):
        super().display_details()
        print("Salary :", self.salary)


per_emp = Permanent_Employee('sneha', 'cse', 10000)
per_emp.display_details()
temp_emp = Temporary_Employee('varsha', 'ece' , 5000)
temp_emp.display_details()