#  Write a function called is_sorted that takes a list as a parameter and returns True
# if the list is sorted in ascending order and False otherwise. You can assume (as a precondition) that
# the elements of the list can be compared with the relational operators <, >, etc.
# For example, is_sorted([1,2,2]) should return True and is_sorted(['b','a']) should return
# False.


def is_sorted(lst):
    count = 0
    flag = False
    for j in range(0, len(lst)):
        for k in range(j + 1, len(lst)):
            if lst[j] <= lst[k]:
                count = count + 1
            else:
                flag = True
                break
        if flag:
            break
    return flag


range1 = int(input("Enter a range"))
lst = []
for i in range(0, range1):
    num = input("enter elements of list")
    lst.append(num)
flag = is_sorted(lst)
if flag:
    print("Not a Sorted List")
else:
    print("Sorted List")
