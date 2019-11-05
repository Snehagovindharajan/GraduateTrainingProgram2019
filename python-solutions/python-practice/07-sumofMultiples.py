# 7:Find the sum of multiples of 3 and 5 between 1 to 1000

list1 = []
sum = 0
for i in range(1,1000):
    if i % 3 == 0 and i % 5 == 0:
        list1.append(i)
for i in range(len(list1)):
    sum = sum + i
print(sum)