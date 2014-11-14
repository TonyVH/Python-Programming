# convert.py
# A program to conver Celsius temperatures to Fahrenheit

def main():
    print('This program will convert Celsius to Fahrenheit')
    celsius = eval(input('What is the celsius temperature? '))
    fahrenheit = 9/5 * celsius + 32
    print('The temperature is', fahrenheit, 'degrees Fahrenheit.')
    
main()
