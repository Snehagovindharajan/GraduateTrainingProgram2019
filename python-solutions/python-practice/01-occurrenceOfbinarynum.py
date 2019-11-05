# 1:For the below binary number , count the Occurrence of sequence '101'
# 10101010100111101
import re
string = "10101010100111101"
count = 0
# str1 = re.findall('[1][0][1]',string)
for i in range(len(string)):
    if i != len(string)-1 and i != len(string)-2:
        if string[i] == '1' and string[i+1] == '0' and string[i+2] == '1':
            count = count + 1
print(count)