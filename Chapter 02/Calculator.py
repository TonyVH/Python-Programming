# Calculator.py
# This is a simple, interactive calulator program
def calculator():
    print('Calculator guide:')
    print('Use + to add')
    print('Use - to subtract')
    print('Use * to multiply')
    print('Use / to divide')
    print('Use ** for exponentials')
    print('Use // for floor division')
    print('Use % to find the remainder of two numbers that cannot divide equally')
    print()

    x = eval(input('Enter your equation here: '))
    print (x)
    print()

    while 1 != 2:
        return calculator()

calculator()
