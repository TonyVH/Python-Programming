# babysitter.py
# Program to calculate the cost to hire a babysitter

def main():
    print('The rate to hire a babysitter is $2.50 and hour before 2100 (9pm), and $1.75 an hour after 2100 (9pm)')

    start = int(input('Enter the start time (use military time): '))
    end = int(input('Enter the end time (using military time): '))

    if end < start:
        end += 2400

    if start < 2100:
        if end <= 2100:
            total = (end-start)*2.50
        else:
            total = (2100-start)*2.50 + (end-2100)*1.75
    else:
        total = (end-start)*1.75
        
    print('The total comes to {0:0.2f}.'.format(total/100))

if __name__=='__main__':
    main()
    
