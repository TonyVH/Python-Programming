# pizza.py
# Program to calculate the area and cost per 
# square inch of a pizza

import math


def area(diameter):
    area = math.pi*((diameter/2)**2)
    return area


def costPerSqIn(area, cost):
    costPer = cost/area
    return costPer


def main():
    diameter, cost = eval(input('Enter the diameter of the pizza and then the cost of the pizza (i.e. 12, 15.99): '))

    pizzaArea = area(diameter)
    CPSI = costPerSqIn(pizzaArea, cost)

    print('The area of the pizza is {0:0.2f} sq. inches, and the cost per sq. inch is ${1:0.2f}.'.format(pizzaArea, CPSI))


main() 
