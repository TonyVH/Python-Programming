# chill.py
# Program to calculate wind chill given the temperature in
# fahrenheit and the wind speed.

def main():
    # Title
    print('{0:^98}'.format('WIND CHILL'))
    print()

    # Create columns of fahrenheit temperatures.
    print(' '*3, end='')
    for temp in range(-20,70,10):
        if temp <= 50:
            print('{0:>10}'.format(temp), end='')
        else:
            print('{0:>10}'.format(temp))

    print(' '*5 + '_'*91)

    # Create rows of wind speeds followed by wind chills in
    # the corresponding temperature columns.
    vel = 5
    while vel <= 50:
        print(' '*4 + '|')
        print('{0:>4}|'.format(vel), end='')
        for temp in range(-20,70,10):
            chill = 35.74 + 0.6215*temp - 35.75*(vel**0.16) + 0.4275*temp*(vel**0.16)
            if temp < 60:
                print('{0:>10.2f}'.format(chill), end='')    
            else:
                print('{0:>10.2f}'.format(chill))
        vel += 5

    print()

if __name__=='__main__':
    main()
    
