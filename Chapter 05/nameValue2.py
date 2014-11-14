# nameValue2.py
# Program to find the numeric value of a name

def main():
    name = input('Please enter your name: ').lower()

    letters = ' abcdefghijklmnopqrstuvwxyz'

    result = 0
    for let in name:
        result += letters.find(let)

    print(result)
    print()

main()
