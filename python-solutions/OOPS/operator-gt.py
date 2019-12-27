class mark:
    def __init__(self,mark1,mark2):
        self.mark1 = mark1
        self.mark2 = mark2
    def __gt__(self, other):
        stu1 = self.mark1 > other.mark1
        stu2 = self.mark2 > other.mark2
        return stu1,stu2

s1 = mark(50,80)
s2 = mark(70,60)
s3 = s1 > s2
print(s3)