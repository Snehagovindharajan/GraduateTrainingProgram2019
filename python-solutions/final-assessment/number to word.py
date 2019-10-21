num_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
num_tens = {1: 'ten', 2: 'twenty', 3: 'thirty', 4: 'fourty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty',
            9: 'ninety'}
number = 4880
word_list = []
rem = number // 1000
word_list.append(num_dict[rem] + " thousand")
rem1 = number // 100
digit = rem1 % 10
word_list.append(num_dict[digit] + " hundred and")
rem2 = number // 10
digit1 = rem2 % 10
rem3 = number % 10
if rem3 == 0:
    word_list.append(num_tens[digit1])
else:
    word_list.append(num_tens[digit1] + " " + num_dict[rem3])
print(" ".join(word_list))
