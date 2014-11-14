# wordfreq.py

def byFreq(pair):
    return pair[1]

def main():
    print('This program analyzes word frequency in a file')
    print('and print a report on ht en most freqent words.\n')

    # Get the sequence of words from the file
    fname = input('File to analyze: ')
    text = open(fname, 'r').read()
    text = text.lower()
    for ch in '!"#$%()*+,-/:;<=>?@[\\]^_{|}~':
        text = text.replace(ch, ' ')
    words = text.split()

    # Construct a dictionary of word counts
    counts = {}
    for w in words:
        counts[w] = counts.get(w,0) + 1

    # Output analysis of n most frequent words
    n = int(input('Output analysis of how many words? '))
    items = list(counts.items())
    items.sort()
    items.sort(key=byFreq, reverse=True)
    try:
        for i in range(n):
            words, count = items[i]
            print('{0:<15}{1:>5}'.format(words, count))
    except IndexError:
        print('There were only {0} words in {1}.'.format(len(items), fname))



if __name__ == '__main__':
    main()
