# exam_grade.py
# Program to score an exam base on a 100 point scale

def main():
    score = eval(input('What was the student\'s exam score? '))

    grades = ['F', 'D', 'C', 'B', 'A']

    if score in range(90, 101):
        result = grades[4]
    elif score in range(80, 90):
        result = grades[3]
    elif score in range(70, 80):
        result = grades[2]
    elif score in range(60, 70):
        result = grades[1]
    elif score in range(0, 60):
        result = grades[0]
    else:
        return main()

    print(result)

main()
