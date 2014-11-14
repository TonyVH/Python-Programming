def main():
    print('This program will calculate the future value over a specified period of time on a principle amount.')
    
    year = eval(input('Enter the amount of years over which you wish to calculate the interest: '))
    principle = eval(input('Input the principle amount: '))
    apr = eval(input('input the annual percentage rate in decimal form: '))

    for i in range(year):
        print(i,'  ', principle)
        principle = principle * (1 + apr)

    print(i + 1, '  ', principle)

main()
