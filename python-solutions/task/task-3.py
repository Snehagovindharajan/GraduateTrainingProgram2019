import re

string = """Hakka and Bukka were brothers and warriors. The brothers wanted to build their own kingdom where people could live without fear. They collected a band of young men and trained them in warfare. They lived in a forest hideout on the banks of the river Tungabhadra in South India.
One day, the brothers were out on a hunt. Ferocious dogs accompanied them. They crossed the river and rode on. A couple of frightened rabbits ran out of the bushes. The dogs gave them chase with the two brothers closely behind on their horses.
It was a long chase. The rabbits were running for their life. The dogs were catching up. Suddenly, in a swift move, the rabbits turned and faced the dogs. Taken aback by the show of defiance, the barking dogs stepped back. Hakka called back the dogs. As the dogs turned back, the rabbits walked away.
Hakka looked around. They were on the other side of the Tungabhadra. It was a rocky land. The sun was blazing in the sky.
“Strange! I’ve never seen rabbits challenging dogs before!” said Bukka.
“That’s the quality of this land,” said a quiet voice, “Even rabbits give fight.”
Startled to hear a stranger speak, the two brothers turned.
They saw a holy man walking towards them. He was a picture of peace. At the same time, his eyes were blazing bright."""
print(len(string))
str1 = string.replace('.', "").replace(',', "").replace('!', "").replace('\"', "").replace('\n',"")
lst = str1.split(" ")
dict1 = {}
list2 = []

print(len(lst))

for i in lst:
    dict1.update({i: lst.count(i)})
print("dictionary : ", dict1)

max1 = 0
char = ''
for i, j in dict1.items():
    if j > max1:
        max1 = j
        char = i
print("Max Occurring Char : ", char)
print("Max Occurring : ", max(dict1.values()))
