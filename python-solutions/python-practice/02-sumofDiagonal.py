# 2: For the below matrix , calculate both the diagonal and print the value.(Hint: consider each row as a list object)
# 3 8 7
# 8 7 9
# 1 6 0
def calsum(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                sum = sum + matrix[i][j]
    return sum


def reversematrix(matrix):
    list1 = []
    for i in matrix:
        lst = reversed(i)
        list1.append(list(lst))
    return list1


matrix = [[3,8,7],[8,7,9],[1,6,0]]
result = calsum(matrix)
matrix1 = reversematrix(matrix)
res = calsum(matrix1)
print(result,res)