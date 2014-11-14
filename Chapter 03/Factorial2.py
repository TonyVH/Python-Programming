# Factorial2.py

def main():
    print('This program will calculate the factorial of a given number.\n')

    x = eval(input('Enter the number you wish to find the factorial for: '))
    
    for num in range(1, x):
        x = x * num
    print(x)

main()
