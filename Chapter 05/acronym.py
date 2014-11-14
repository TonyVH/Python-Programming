# acronym.py
# Program to create an acronym from a user given sentence/phrase

def main():
    print('This program will create an acronym from a word or phrase\n')
    phrase = input('Enter a sentence or phrase: ')

    phrase = phrase.split()
    for words in phrase:
        print(words[0].upper(), end='')

    print()

main()
