# gpa.py
# Program that calculates the GPA for each student in a file,
# and then prints out who has the hightest GPA.

class Student:

    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints/self.hours

    def addGrade(self, gradePoint, credits):
        if gradePoint == 4.0:
            return 'A'
        elif 3.7 <= gradePoint < 4.0:
            return 'A-'
        elif 3.3 <= gradePoint < 3.7:
            return 'B+'
        elif 3.0 <= gradePoint < 3.3:
            return 'B'
        elif 2.7 <= gradePoint < 3.0:
            return 'B-'
        elif 2.

def makeStudent(infoStr):
    # infoStr is a tab-separated line: name hours qpoints
    # returns a corresponding Student object
    name, hours, qpoints = infoStr.split("\t")
    return Student(name, hours, qpoints)

def main():
    # Open file of student names, hours, and qpoints
    file = input("Enter file name: ")
    infile = open(file, "r")

    # Set best to the record for the first student in the file
    best = makeStudent(infile.readline())

    # Process subsequent lines of the file
    for line in infile:
        # Turn the line into a student record
        s = makeStudent(line)
        # If this student is best so far, remember it
        if s.gpa() > best.gpa():
            best = s

    infile.close()

    # Print information about the best student
    print("The best student is: {}".format(best.getName()))
    print("Hours: {}".format(best.getHours()))
    print("GPA: {}".format(best.gpa()))

if __name__ == "__main__":
    main()
    
