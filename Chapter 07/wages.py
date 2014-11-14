# wages.py
# Program to calculate weekly wages, including any overtime pay

def main():
    rate = eval(input('Enter your hourly pay rate: '))
    hours = eval(input('Enter the number of yours you worked this week: '))

    if hours <= 40:
        wages = rate*hours
    elif hours > 40:
        wages = 40*rate + ((hours-40)*(rate*1.5))
    else:
        print('Either something went wrong, or you did not work this week.')

    print('Your wages before anything is taken out is {0}.'.format(wages))

if __name__=='__main__':
    main()
