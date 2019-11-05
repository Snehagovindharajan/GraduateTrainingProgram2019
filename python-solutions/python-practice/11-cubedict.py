# With a given integral number n, change the program to generate a dictionary that contains (i, cube of i) such that
# is an integral number between 1 and n (both included). and then the program should print the dictionary. Suppose
# the following input is supplied to the program: 7 Then, the output should be: {1: 1, 2: 8, 3: 27, 4: 64, 5: 125,
# 6: 216, 7: 373} Take the input from the user via console.

rnge = int(input("Enter a number"))
cube_dict = {}
for i in range(1, rnge + 1):
    cube_dict.update({i: pow(i, 3)})
print(cube_dict)
