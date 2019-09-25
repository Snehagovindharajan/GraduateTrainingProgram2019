# 2. Define a class Person and its two child classes: Male and Female.
# All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.


class Person:
    def getGender(self):
        print("Gender is ",end='')


class Male(Person):
    def __init__(self, gender):
        self.gender = gender

    def getGender(self):
        super().getGender()
        print("Male")


class Female(Person):
    def __init__(self, gender):
        self.gender = gender

    def getGender(self):
        super().getGender()
        print("Female")


gender = input("Enter Gender 'f'/'F'/'m'/'M'")
if gender == 'F' or gender == 'f':
    female = Female(gender)
    female.getGender()
else:
    male = Male(gender)
    male.getGender()
