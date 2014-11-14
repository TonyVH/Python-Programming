# numbers2text.py
# A program to convert a sequence of Unicode numbers into a string of text.

def main():
    print('This program converts a sequence of Unicode numbers into')
    print('the string of text that it represents.\n')

    # Get the message to encode
    inString = input('Please enter the unicode-encoded message: ')

    # Loop through each substring and build Unicode message
    chars = []
    for numStr in inString.split():
        codeNum = eval(numStr) # Convert digits to a number
        chars.append(chr(codeNum)) # Accumulate new character

    message = ''.join(chars)
    print('\nThe decoded message is:', message)

main()
