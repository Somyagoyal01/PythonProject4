""" Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results."""
import math
num=int(input("Enter your number= "))
def sqrt(n):
    a=(math.sqrt(n))
    print(a)
sqrt(num)
def log(m):
    b=(math.log(m))
    print(b)
log(num)
def sine(p):
    c=(math.sin(p))
    print(c)
sine(num)

