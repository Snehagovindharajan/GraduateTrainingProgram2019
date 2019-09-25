# Write a function called is_abecedarian that returns True if the letters in a word
# appear in alphabetical order (double letters are ok). How many abecedarian words are there?
# (i.e) "Abhor" or "Aux" or "Aadil" should return "True"  Banana should return "False"


def is_abecedarian(string):
    count = 0
    flag = False
    for i in range(0, len(string)):
        for j in range(i + 1, len(string)):
            if string[i] <= string[j]:
                # print(string[i],string[j],i,j)
                count = count + 1
            else:
                flag = True
                break
        if flag:
            break
    return flag


string = [i for i in input("Enter a string").split(',')]
for i in string:
    flag = is_abecedarian(i)
    if flag:
        print(i, " is Not a Sorted String")
    else:
        print(i, "is a Sorted String")