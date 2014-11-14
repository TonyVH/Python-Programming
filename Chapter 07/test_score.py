# test_score.py
# Program to calculate the letter grade of a test score

def main():
    score = eval(input('Enter the student\'s test score: '))

    if score >= 90:
        grade = 'A'
    elif score in range(80,90):
        grade = 'B'
    elif score in range(70,80):
        grade = 'C'
    elif score in range(60,70):
        grade = 'D'
    else:
        grade = 'F'

    print('The student\'s test grade is {0}.'.format(grade))

if __name__=='__main__':
    main()
