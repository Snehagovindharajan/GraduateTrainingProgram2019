class Person:
    def __init__(self, name):
        self.name = name
    # def display(self):
    #     print("Name :", self.name)


class Student:
    def __init__(self, standard, section):
        self.standard = standard
        self.section = section

    # def display(self):
    #     print("Standard :", self.standard, "Section :", self.section)


class School(Student, Person):
    def __init__(self, name, standard, section, school_name):
        Student.__init__(self, standard, section)
        Person.__init__(self, name)
        self.school_name = school_name

    def display(self):
        # super().display()
        print("Name :", self.name, "Standard :", self.standard, "Section :", self.section, "School_name :",
              self.school_name)


school = School('sneha', '12th', 'A2', 'velammal')
school.display()
