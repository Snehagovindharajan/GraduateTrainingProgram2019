# Write a python script to validate the strong password (combination of characters alphabets and numbers,
# special characters in it. if not weak password) eg: Acc9876$ it is strong password abcd it is weak password
password = ['ABd1234@1', 'a F1#', '2w3E*', '2We3345', 'Acc9876$', 'abcd']
for pass_word in password:
    upper = False
    lower = False
    number = False
    special = False
    other = False
    if 6 < len(pass_word) < 12:
        for letter in pass_word:
            if 65 <= ord(letter) <= 90:
                upper = True
            elif 97 <= ord(letter) <= 122:
                lower = True
            elif 48 <= ord(letter) <= 57:
                number = True
            elif ord(letter) == 35 or ord(letter) == 36 or ord(letter) == 64:
                special = True
            else:
                other = True
    if lower == True and upper == True and number == True and special == True and other == False:
        print(pass_word, " is a strong password")
    else:
        print(pass_word, " is a week password")
