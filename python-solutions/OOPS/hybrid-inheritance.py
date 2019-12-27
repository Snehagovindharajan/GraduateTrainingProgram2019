class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, standard, section):
        Person.__init__(self,name)
        self.standard = standard
        self.section = section

    def display(self):
        print(" Student Name :", self.name, "Standard :", self.standard, "Section :", self.section)


class Faculty(Person):
    def __init__(self, name, standard, section):
        Person.__init__(self,name)
        self.standard = standard
        self.section = section

    # def display(self):
    #     print("Faculty Name :", self.name, "Standard :", self.standard, "Section :", self.section)


class School(Faculty, Student):
    def __init__(self, name, standard, section, school_name):
        super().__init__(name, standard, section)
        self.school_name = school_name

    def display(self):
        super().display()
        print("School_name :", self.school_name)


school = School('sneha', '12th', 'A2', 'velammal')
school.display()
