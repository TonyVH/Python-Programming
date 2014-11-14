# File: chaos.py
# A siple program illustrating chaotic behavior.

def main():
    print('This program illustrates a chaotic function')
    print('List 1')
    n = eval(input('How many numbers should I print?: '))
    x = eval(input('Enter a decimal number between 0 and 1: '))
    print('List 2')
    y = eval(input('Enter a decimal number between 0 and 1: '))
    for i in range(n):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print('%.5f  ' % x, '  %.5f' % y)
main()

