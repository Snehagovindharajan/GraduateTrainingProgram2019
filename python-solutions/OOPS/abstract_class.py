from abc import ABC, abstractmethod


class Employee:
    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        pass


class Permanent_Employee(Employee):
    salary = 0

    def __init__(self, name, no_of_hours):
        super().__init__(name)
        self.no_of_hours = no_of_hours
        # self.salary = salary

    def calculate_salary(self):
        self.salary = self.no_of_hours * 150

    def display_details(self):
        print("Name : ", self.name, "Salary : ", self.salary)


per_emp = Permanent_Employee('sneha', 198)
per_emp.calculate_salary()
per_emp.display_details()
