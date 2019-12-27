import sys

try:
    # print("Max : ", max(sys.argv[1], sys.argv[2], sys.argv[3]))
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]
    if a > b and a > c:
        print("Max : ",a)
    elif b > c:
        print("Max : ", b)
    else:
        print("Max : ", c)

except:
    print("Less number of arguments")
