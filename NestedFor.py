# NestedForLoopExample--- Find Pythagorian numbers for the number entered

from math import sqrt

number = int(input("Enter number:"))
for a in range(1, number + 1):
    for b in range(a, number):
        c_square = a ** 2 + b ** 2
        c = int(sqrt(c_square))
        if ((c_square - c ** 2) == 0):
            print(a, b, c)
