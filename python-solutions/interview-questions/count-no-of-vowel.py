vowel = 'aeiou'
c = {}.fromkeys(vowel, 0)
ip_str = 'Noah Centineo'
for ichar in ip_str:
    if ichar in vowel:
        c[ichar] += 1
print(c)

string = 'Noah Centineo'
count_vowel = {}
for i in string:
    if i in 'aeiou':
        count_vowel.update({i: string.count(i)})
print(count_vowel)