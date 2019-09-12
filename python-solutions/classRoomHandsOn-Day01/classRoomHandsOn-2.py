# Get ur full name, age as input from user and print first name and last name , age using string slicing a) 2
# raw_input get name and age b) print first name and last name and age c) WHEN age >= 18 , he/she is eligible to vote
# d) WHEN age < 18 , he/she is not eligible to vote
from pip._vendor.distlib.compat import raw_input

details = raw_input("Enter your name and age")
#age = input("Enter your age")
lst=details.split()
print("First Name : "+lst[0])
print("Last Name : "+lst[1])
print("Age : "+lst[2])

if(lst[2] < '18'):
    print("he/she is Not eligible to vote")
else:
    print("he/she is Eligible to vote")

