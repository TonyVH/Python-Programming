# triangle.py
# program to calculate the area of a triangle

import math

def s(a, b, c):
    s = (a+b+c)/2
    return s

def area(s, a, b, c):
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area

def main():
    a, b, c = eval(input('Enter the length of the three sides of the triangle (i.e. 4, 4, 5): '))

    sTriangle = s(a, b, c)
    triArea = area(sTriangle, a, b, c)

    print('The area of the triangle is {0:0.2f}.'.format(triArea))

main() 


     

