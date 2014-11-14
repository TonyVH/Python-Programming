# BMI.py
# Calculates Body Mass Index and prints our if
# the user is in, aobve, or below the healthy range

def main():
    pounds = eval(input('Enter your weight in pound: '))
    height = eval(input('Enter your height in inches: '))

    BMI = (pounds*720)/(height**2)

    if BMI < 19:
        health = 'below'
    elif BMI > 25:
        health = 'above'
    else:
        health = 'within'

    print('Your BMI is {0} and is {1} the healthy range.'.format(BMI, health))

if __name__=='__main__':
    main()
