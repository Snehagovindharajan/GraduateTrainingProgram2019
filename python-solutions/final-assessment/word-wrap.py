import textwrap
import re

# value = "Hi, this is sample text."
# num = 9
# wrapper = textwrap.TextWrapper(width= 9)
# word_list = wrapper.wrap(text=value)
# for element in word_list:
#     print(element)

sample_text = "Hi, this is sample text."
column_range = 9
split_text = list(sample_text)
for i in range(0, len(split_text)):
    sample_text = ''.join(split_text)

    if len(split_text) < column_range:
        print("".join(split_text).strip(" "))
        break

    elif split_text[column_range] == ' ':
        str1 = ''
        for j in range(0, column_range):
            str1 = str1 + split_text[j]
        print(str1.strip(" "))
        for k in range(0, column_range):
            split_text.remove(split_text[0])

    else:
        index_list = []
        maxi = 0
        for i in re.finditer(" ", sample_text):
            if i.start() < column_range:
                index_list.append(i.start())
        maxi = max(index_list)
        str1 = ''
        for j in range(0, maxi + 1):
            str1 = str1 + split_text[j]
        print(str1.strip(" "))
        for k in range(0, maxi+1):
            split_text.remove(split_text[0])