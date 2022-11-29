def getAvgFunction(numStudents):
    t1 = int(input('Enter test score 1:', ))
    t2 = int(input('Enter test score 2:', ))
    t3 = int(input('Enter test score 3:', ))
    avg = float(int(t1 / 3) + (t2 / 3) + (t3 / 3))
    return avg


students = input('How many students are in the class?: ')
studentsInClass = int(float(students))
numStudents = [0 for i in range(studentsInClass)]
numTest = 3
testAvg = [0 for j in range(numTest)]
scoreTotal = 0

for i in range(studentsInClass):
    numStudents[i] = input("Student Name:")
    scoreTotal = 0
    studentName = 1
    for j in range(studentName):
        testAvg[j] = getAvgFunction(numStudents[i])
        scoreTotal += testAvg[j]
        average = float(int(round(testAvg[j])))
    print(numStudents[i], 'test average is:', average, '%.')