# eachSquared.py
# Program to square each number in a list

def square(x):
    return x*x

def eachSquared(numList):
    numList = [square(i) for i in numList]
    return numList

def main():
    numbers = input('Enter a list of numbers: ').split()

    numbers = [int(i) for i in numbers]

    newList = eachSquared(numbers)

    print(newList)

main()
