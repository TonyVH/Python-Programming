# username.py
# A simple string processing program to generate usernames based on the user's actual name

def main():
    # Introduction
    print('This program generates computer usernames.\n')

    # Get user's first and last names
    first = input('Please enter your first name: ').lower()
    last = input('Please enter your last name: ').lower()

    # Concatenate first initial with 7 characters of the last name
    uname = first[0] + last[:7]

    # Output the username
    print('Your username is: ', uname)

main()
