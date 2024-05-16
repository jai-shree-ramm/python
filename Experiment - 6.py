from math import pi, pow
def area(r):
    return pi * pow(r, 2)
r = float(input("Enter the radius: "))
print("Area of circle:", area(r)) 
