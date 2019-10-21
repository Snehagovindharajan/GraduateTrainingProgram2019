# expression = "{([8+3])*([1+2])}"
expression = "{(([8+3)])*(1+2)])}"
expre_list = list(expression)
paran_dict = {'(': ')', '{': '}', '[': ']'}
open_paran = []
close_paran = []
flag = True
for i in expre_list:
    if i in '({[':
        open_paran.append(i)
    elif i in ')}]':
        close_paran.append(i)
open_paran.reverse()
if len(open_paran) == len(close_paran):
    for i in range(len(open_paran) - 1, -1, -1):
        for j in range(i, len(close_paran)):
            if close_paran[j] == paran_dict[open_paran[i]]:
                flag = True
                break
            else:
                flag = False
                break
        if flag == False:
            print("Invalid")
            break
    if flag:
        print("Valid")
else:
    print("Invalid")
