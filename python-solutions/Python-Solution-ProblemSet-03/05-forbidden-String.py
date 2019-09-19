#  Write a function named avoids that takes a word and a string of forbidden letters,
# and that returns True if the word doesn’t use any of the forbidden letters.

def avoids(string, forbidden_string):
    for i in forbidden_string:
        if i in string:
            print("the word use one of the forbidden letters")
            break
    else:
        print("the word doesn’t use any of the forbidden letters")


string = input("Enter a string")
forbidden_string = input("Enter a forbidden_string ")
avoids(string, forbidden_string)
