class Employee:
    def __init__(self, name):
        self.name = name


class Permanent_Employee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def display_details(self):
        print("Name : ", self.name, "Salary : ", self.salary)


per_emp = Permanent_Employee('sneha',10000)
per_emp.display_details()
