class Course:
    CRN = None
    Course_id = None
    Instructor = None
    NumberCredits = None


user_input = int(input("How many courses would you like to add?: ", ))
Course1 = Course()
array = [Course() for i in range(user_input)]

for i in range(int(user_input)):
    array[i].CRN = input("What is the CRN for this course?: ", )
    array[i].Course_id = input('What is the course id?: ', )
    array[i].Instructor = input('Who is the instructor?:', )
    array[i].NumberCredits = input("What is the number of credits for this course?:", )
print()

for i in range(int(user_input)):
    print("CRN number: ", array[i].CRN, ' Course ID: ',array[i].Course_id, ' Instructor: ', array[i].Instructor, 'Credits: ', array[i].NumberCredits)
