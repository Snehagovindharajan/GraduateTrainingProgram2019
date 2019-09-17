# A palindrome is a word that is spelled the same backward and forward, like "Malayalam"
# and "Noon" . Recursively, a word is a palindrome if the first and last letters are the same and the
# middle is a palindrome.
# Write a function called is_palindrome that takes a string argument and returns True if it
# is a palindrome and False otherwise. Remember that you can use the built-in function len
# to check the length of a string.
# Use the function definition
# ```python
# def isPalindrome(s):
# 	"""Assumes s is a str
# 	Returns True if s is a palindrome; False otherwise.
# 	Punctuation marks, blanks, and capitalization are
# 	ignored."""
# ```
# Ensure you build a test function testIsPalindrome() that tests your palindrome function.


def isPalindrome(str1):
    str2 = ''
    for i in range(len(str1) - 1, -1, -1):
        str2 = str2 + str1[i]
    if str2 == str1:
        return True
    else:
        return False


def testisPalindrome():
    string = input("Enter a String")
    string = string.lower()
    result = isPalindrome(string)
    if (result):
        print("Palindrome")
    else:
        print("Not a Palindrome")

testisPalindrome()
