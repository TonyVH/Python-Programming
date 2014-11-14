# dateConvert.py
# Converts day month and year numbers into two date formats

def main():
    # Get the day month and year
    day, month, year = eval(input('Enter day, month, and year numbers (separated by a comma): \n'))

    date1 = '{0}/{1}/{2}'.format(month, day, year)

    months = ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December']

    monthStr = months [month-1]
    date2 = '{0} {1}, {2}'.format(monthStr, day, year)

    print('The date is {0} or {1}.'.format(date1, date2))

main()
