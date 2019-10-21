expression = "{([8+3])*([1+2])}"
expre_list = list(expression)
list_expre = []
# dict_expre = {}
dict_paran = {')': '(', ']': '[', '}': '{', '{':'', '(':'', '[':''}
# flag = False
for i in expre_list:
    if i in ['{', '}', '[', ']', '(', ')']:
        list_expre.append(i)
        print(list_expre)
        for j in range(0, len(list_expre)):
            if len(list_expre) > 1:
                print(list_expre[j], list_expre[j-1], dict_paran[list_expre[j]])
                if list_expre[j-1] == dict_paran[list_expre[j]]:
                    list_expre.remove(list_expre[j])
                    print(list_expre)
                    list_expre.remove(dict_paran[list_expre[j]])
print(list_expre)

# print(list_expre)
# for i in list_expre:
#     dict_expre.update({i:list_expre.count(i)})
# print(dict_expre)
# for key, value in dict_expre.items():
#     if value % 2 != 0:
#         flag = True
#         break
# if flag:
#     print("Invalid expression")
# else:
#     print("valid expression")
