def tutorial_details(name, session='Python'):
    print("Name : ", name)
    print("Age : ", session)


name = input("Enter Name")
session = input("Enter Session")
tutorial_details(name)
tutorial_details(name,session)
