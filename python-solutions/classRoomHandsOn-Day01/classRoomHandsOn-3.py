# Calculating your birth number in numerology 26/11/1978 2+6+1+1+1+7+8 = 8

date = input("Enter a date dd/mm/yyyy")
lst=list(date)
#print(lst)
lst.remove(lst[7])
for i in lst:
    if(i == '/'):
        lst.remove(i)
#print(lst)
sum = 0
for j in range(0,len(lst)):
    sum = sum + int(lst[j])
#print(sum)
st = str(sum)
lst1 = list(st)
sum = 0
for j in range(0,len(lst1)):
    sum = sum + int(lst1[j])
print(sum)