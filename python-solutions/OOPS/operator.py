class mark:
    def __init__(self,mark1,mark2):
        self.mark1 = mark1
        self.mark2 = mark2
    def __add__(self, other):
        stu1 = self.mark1 + other.mark1
        stu2 = self.mark2 + other.mark2
        return stu1,stu2

s1 = mark(50,60)
s2 = mark(70,80)
s3 = s1 + s2
print(s3)
from abc import abstractmethod

# class Duck:
#     def Quack(self):
#         print("Duck")
#
#     def test(object):
#         if isinstance(object, Duck):
#             object.Quack()
# class Person:
#     def Quack(self):
#         print("Person")
#
#     def test(object):
#         if isinstance(object, Duck):
#             object.Quack()
#
#
# d1 = Duck()
# d1.test()
# p1 = Person()
# p1.test()