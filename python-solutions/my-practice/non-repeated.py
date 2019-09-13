# How do you print the first non-repeated character from a string
name = input("Enter a name")
for i in name:
    if (name.count(i) == 1):
        print(i)
        break