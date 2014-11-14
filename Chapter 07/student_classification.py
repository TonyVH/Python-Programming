# student_classification.py
# Program to calculate if a student is a Freshman, Sophomore, 
# Junior, or Senior based on credits earned

def main():
    credits = eval(input('Enter the number of credits the student has earned: '))

    if credits < 7:
        classification = 'Freshman'
    elif credits in range(7,16):
        classification = 'Sophomore'
    elif credits in range(16,26):
        classification = 'Junior'
    else:
        classification = 'Senior'

    print('This student is a {0}.'.format(classification))

if __name__=='__main__':
    main()


