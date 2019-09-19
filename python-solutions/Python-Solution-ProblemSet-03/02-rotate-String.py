# Write a function called rotate_word() that takes a string and an integer as parameters, and that
# returns a new string that contains the letters from the original string "rotated" by the given amount.
# For example, "cheer" rotated by 7 is "jolly" and "melon" rotated by -10 is "cubed".
# You might want to use the built-in functions ord, which converts a character to a numeric code,
# and chr, which converts numeric codes to characters.


def rotate_word(string, inc):
    str1 = ''
    for i in range(0, len(string)):
        asc = ord(string[i]) + inc
        if asc > 122:
            length = asc - 122
            length = 97 + length - 1
            asc = length
        if asc < 97:
            length = 97 - asc
            length = 122 - length + 1
            asc = length
        str1 = str1 + chr(asc)
    return str1


string = input("Enter a string")
inc = int(input("Enter increment value"))
result = rotate_word(string, inc)
print(result)
