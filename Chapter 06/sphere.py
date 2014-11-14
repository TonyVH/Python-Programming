# sphere.py
# Program to find the volume and surface area of a sphere

import math

def volume(radius): 
    vol = (4/3)*math.pi*(radius**3)
    return vol

def surArea(radius):
    area = 4*math.pi*(radius**2)
    return area

def main():
    rad = eval(input('Enter the radius of the sphere: '))


    v = volume(rad)
    sa = surArea(rad)

    print('The volume of the sphere is {0:0.2f}, and the surface area of the sphere is {1:0.2f}.'.format(v, sa))

main() 
