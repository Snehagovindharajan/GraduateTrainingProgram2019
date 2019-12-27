def subject(stud_name, **argv):
    print("Student Name : ", stud_name)
    print("Marks : ", argv)


subject("sneha", science=78, maths=98, social=68)
subject("jam", science=78, maths=98)
