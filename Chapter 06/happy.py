# happy.py
# Program to sing happy birthday

def happy():
    print('Happy Birthday to you!')

def sing(person):
    happy()
    happy()
    print('Happy Birthday dear {0}!'.format(person))
    happy()

def main():
    sing('Becky')
    print()
    sing('Judah')
    print()
    sing('Analeigh')

main()
