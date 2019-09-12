# a. What would the code above return if the statement x = 25
# were replaced by x = -25?
#
# b. What would have to be changed to make the code above
# for finding an approximation to the cube root of both negative and
# positive numbers? (Hint: think about changing low to ensure that the answer
# lies within the region being searched.)

x = -25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)  # 25
ans = (high + low) / 2.0  # 17.5 # 0.5
while abs(ans ** 2 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)  # 0.0 , 25 , 12.5

numGuesses += 1  # 1
if ans ** 2 < x:  # false
    low = ans
else:
    high = ans  # high = 17.5
    ans = (high + low) / 2.0  # 17.5
print('numGuesses =', numGuesses)
print(ans, 'is close to square root of', x)
