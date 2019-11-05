# 3 :Rotate the above matrix by 90 degree anticlockwise
# hint :convert row to column and column to row

def reversematrix(matrix):
    list1 = []
    for i in matrix:
        lst = reversed(i)
        list1.append(list(lst))
    return list1


def rotate(result):
    for i in range(len(result)):
        for j in range(len(result[i])):
            print(result[j][i], end="")
        print("\n")


matrix = [[3, 8, 7], [8, 7, 9], [1, 6, 0]]
res = reversematrix(matrix)
print(res)
rotate(res)
