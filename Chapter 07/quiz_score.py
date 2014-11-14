# quiz_score.py
# Program to calculate a letter grade based on correct answers 

def main():
    score = eval(input('Enter the number of correct answers the student got: '))

    if score >= 5:
        grade = 'A'
    elif score == 4:
        grade = 'B'
    elif score == 3:
        grade = 'C'
    elif score == 2:
        grade = 'D'
    else:
        grade = 'F'

    print('The student\'s letter grade is {0}.'.format(grade))

if __name__=='__main__':
    main()
