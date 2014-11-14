# quiz_grade.py
# Program to grade a five point quiz

def main():
    score = eval(input('How many correct questions did the student answer? '))

    grades = ['F','F', 'D', 'C', 'B', 'A']

    result = grades[score]

    print(result)

main()
