lst = ['34', '67', '55', '33', '12', '98']
sum = 0
for i in lst:
    if int(i) % 2 == 0:
        sum = sum + int(i)
print(sum)