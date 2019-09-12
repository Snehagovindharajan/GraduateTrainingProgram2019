# Practice using the Python interpreter as a calculator:
# 	```
# 	a) The volume of a sphere with radius r is 4/3pr3. What is the volume of a sphere with radius 5?
# 	Hint: 392.7 is wrong!
#     b) Suppose the cover price of a book is Rs.24.95, but bookstores get a 40% discount. Shipping costs
# 	Rs.3 for the first copy and 0.75p for each additional copy. What is the total wholesale cost for
# 	60 copies?
#     c) If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at
# 	tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?

# 100p = 1Rs
# a)
radius = int(input("Enter a radius"))
volume = (4 / 3) * 3.14 * pow(radius, 3)
print("volume of a sphere :  ", volume)

# b)
cover_price = float(input("Enter cover price"))  # 24.95
total_book = int(input("Enter total no of books"))  # 60

total_book_cost = total_book * cover_price
dis_cost = total_book_cost * (40 / 100)
actual_book_cost = total_book_cost - dis_cost

actual_book = total_book - 1
overall_cost = (actual_book * 0.75) + actual_book_cost + 3
print(overall_cost)
