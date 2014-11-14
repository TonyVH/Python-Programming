# eachSum.py

def sum(x):
    return x+x

def eachSum(numList):
    numList = [sum(i) for i in numList]
    return numList

def main():
    numbers = input('Enter a list of numbers: ').split()

    numbers = [int(i) for i in numbers]

    newList = eachSum(numbers)

    print(newList)

main()
