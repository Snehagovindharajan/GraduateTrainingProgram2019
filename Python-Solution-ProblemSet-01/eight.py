# Implement a function that satisfies the specification. Use a try-except block.
#
# ```python
# def getRatios(vect1, vect2):
# 	"""Assumes: vect1 and vect2 are lists of equal length of numbers
# 	Returns: a list containing the meaningful values of
# 	vect1[i]/vect2[i]"""
# ```

vect1 = [1,4,27,4,5]
vect2 = [1,2,3,0,5]
list1 = []
try:
    for i in range(0,len(vect1)):
        list1.append(vect1[i]/vect2[i])
        #print(list1)
except:
    print(list1)
    print("Divide by Zero")