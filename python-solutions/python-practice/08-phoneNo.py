# 8: Display the phone number as below and also print the last 4 digit in ascending order
# input : 9993452133
# output :xxx-xxx-xxxx

phoneNo = input("Enter a phone no")
if len(phoneNo) == 10:
    str1 = ''.join(sorted(phoneNo[-1:-5:-1])).strip()
    print("XXX-XXX-", str1)
