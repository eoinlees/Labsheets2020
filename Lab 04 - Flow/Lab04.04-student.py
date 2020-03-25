#Eoin Lees
# A program that reads in students until the user enters a blank
# It prints them all out again

students = []

firstname = input("Enter first name (Blank to quit):").strip()
while firstname != "":
    student = {}
    student["firstname"] = firstname
    lastname = input("Enter last name: ").strip()
    student["lastname"] = lastname
    students.append(student)
    # Next student
    firstname = input("Enter first name (Blank to quit):").strip()

print ("Here are the students you entered: ")
for currentStudent in students:
    print ("{}, {}".format(currentStudent["firstname"], currentStudent["lastname"]))

    