# max.py
# Finds the maximum of a series of numbers

def main(): 
    n = eval(input('How many numbers are there? '))

    # Set max to be the first value
    max = eval(input('Enter a number >> '))

    # Now compare the n-1 successive values
    for i in range(n):
        x = eval(input('Enter a number >> '))
        if x > max:
            max = x

    print('The largest value is {0}.'.format(max))

if __name__=='__main__':
    main()
