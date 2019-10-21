s = "madam"

# method 1
if s == s[::-1]:
    print("palindrome")
else:
    print("Not a Palindrome")

# method 2
str1 = ""
for i in range(len(s)-1,-1,-1):
    str1 = str1 + s[i]
if str1 == s:
    print("palindrome")
else:
    print("Not a palindrome")

# method 3
str2 = ""
for i in range(0,len(s)):
    str2 = s[i] + str2
if str2 == s:
    print("Palindrome")
else:
    print("Not a palindrome")

# method 4
s1 = list(reversed(s))
if s == ''.join(s1):
    print("palindrome")
else:
    print("Not a palindrome")