# word_count.py
# Program to determine the number of lines, words, and characters contained in a file

def main():
    fileName = input('Enter the filename: ')

    infile = open(fileName, 'r')

    # Character count (including new line characters) and line count
    characters = 0
    words = 0
    lines = 0
    for line in infile.readlines():
        characters += len(line)
        lines += line.count(line)

    wordList = []    
    for word in infile.readlines():
        wordList.append(word)


    print(characters, lines, wordList)

main()
