import re

string = """Hakka and Bukka were brothers and warriors. The brothers wanted to build their own kingdom where people 
could live without fear. They collected a band of young men and trained them in warfare. They lived in a forest 
hideout on the banks of the river Tungabhadra in South India. One day, the brothers were out on a hunt. Ferocious 
dogs accompanied them. They crossed the river and rode on. A couple of frightened rabbits ran out of the bushes. The 
dogs gave them chase with the two brothers closely behind on their horses. It was a long chase. The rabbits were 
running for their life. The dogs were catching up. Suddenly, in a swift move, the rabbits turned and faced the dogs. 
Taken aback by the show of defiance, the barking dogs stepped back. Hakka called back the dogs. As the dogs turned 
back, the rabbits walked away. Hakka looked around. They were on the other side of the Tungabhadra. It was a rocky 
land. The sun was blazing in the sky. "Strange! I’ve never seen rabbits challenging dogs before! " said Bukka. 
"That’s the quality of this land, " said a quiet voice,  "Even rabbits give fight. " Startled to hear a stranger 
speak, the two brothers turned. They saw a holy man walking towards them. He was a picture of peace. At the same 
time, his eyes were blazing bright. """
# print("Length Of String : ",len(string))
str1 = string.replace('.', "").replace(',', "").replace('!', "").replace('\"', "").replace('\n',"")
lst = str1.split(" ")
dict1 = {}
list2 = []

# print("Number Of Words : ",len(lst))

for i in lst:
    dict1.update({i: lst.count(i)})
# print("dictionary : ", dict1)

mini = 100
char = ''
lst1 = []
lst2 = []
for i, j in dict1.items():
    if j <= mini:
        mini = j
        char = i
# print("Min Occurring : ", min(dict1.values()))
# print("Min Occurring Word : ", char)

for k,l in dict1.items():
    if dict1[k] == mini:
        lst1.append(k)
        lst2.append(l)
# print("Repeated word's list : ",lst1)
# print("Repeated word's count : ",lst2)

dict2 = {"Length Of String": len(string), "Number Of Words": len(lst), "Max Occurring": max(dict1.values()),
         "Max Occurring Word": char, "Repeated word's list": lst1, "Repeated word's count": lst2}
print(dict2)