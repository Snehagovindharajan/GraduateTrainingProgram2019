# Modify the above program to print only the words that have no “e” and compute the percentage of the words in the list have no “e.”
def has_no_e(str_lst):
    noe_lst = []
    for j in range(0, len(str_lst)):
        if 'e' not in str_lst[j]:
            noe_lst.append(str_lst[j])
    return len(noe_lst)


rang = int(input("Enter a range"))
lst = []
for i in range(0, rang):
    string = input("Enter a string")
    lst.append(string)
result = has_no_e(lst)
percent_e_list = (result / len(lst)) * 100
print("the percentage of the words in the list have no 'e' : ", percent_e_list)
