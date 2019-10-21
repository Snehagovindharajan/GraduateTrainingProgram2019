from abc import abstractclassmethod, ABC


class Employee(ABC):
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)

    @abstractclassmethod
    def cal_salary(self):
        pass


class TemporarySalary(Employee):

    def __init__(self, hours, name):
        super().__init__(name)
        self.hours = hours
        self.sal = 0

    def cal_salary(self):
        self.sal = self.hours * 200

    def display(self):
        print(self.name, self.sal)

class PermanentEmployee(Employee):
    def __init__(self,hours,name):
        super().__init__(name)
        self.hours = hours
        self.sal = 0

    def cal_salary(self):
        self.sal = self.hours * 300

    def display(self):
        print(self.name, self.sal)

Temporary = TemporarySalary(9, 'sneha')
Temporary.cal_salary()
Temporary.display()
Permanent = PermanentEmployee(9, 'jamuna')
Permanent.cal_salary()
Permanent.display()
