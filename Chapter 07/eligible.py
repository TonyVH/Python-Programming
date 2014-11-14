# eligible.py
# Program to determine if someone is eligible for the
# US senate, or the US representatives

def main():
    age = eval(input('Enter your age: '))
    years = eval(input('Enter the number of years you have been a citizen: '))

    if age >= 30 and years >= 9:
        print('You are eligible to run for the senate and house of representatives.')
    elif age in range(25,31) and years >= 7:
        print('You are eligible to run for the house of representatives, but not the senate.')
    else:
        print('You are not eligible to run for the senate or the house of representatives.')

if __name__=='__main__':
    main()
