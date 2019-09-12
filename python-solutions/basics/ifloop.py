"""print value of a"""
a = 1
b = 2
c = a + b
if (a == 0):
    print(a)
else:
    print(a + 1)
print(__doc__)

no = int(input('enter a number'))
if(no % 2 != 0):
    print('Odd','\nnumber',no)
elif(no == 0 ):
    print('Zero')
else:
    print('Even')