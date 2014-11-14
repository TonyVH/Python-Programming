# naturalNumbers.py
# Program to find the sum and cubed values of n natural numbers, 
# where n = a random number given by the caller of the function

def sumN(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum

def sumNCubes(n):
    sum = 0
    for i in range(n):
        sum += i**3
    return sum

def main():
    num = eval(input('Enter how many natural numbers you wish to evaluate: '))

    sum1 = sumN(num)
    sum2 = sumNCubes(num) 

    print('The sum of the first {0} natural numbers is {1}, and the sum of the cubed values of the first {0} natural numbers is {2}.'.format(num, sum1, sum2)) 

main()
 

 
