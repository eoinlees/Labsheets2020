#Eoin Lees


students=[]

def displayMenu():
    print("What would you like to do?:")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a,v,q):").strip()

    return choice

def readModules():
    modules = []
    currentName = input("\t\tEnter module name (blank to end):")
    while currentName != "":
        module = {}
        module["name"] = currentName
        module["grade"] = input ("\t\tEnter grade:")
        modules.append(module)

        currentName = input("\t\tEnter next module name (blank to end):")
    return modules

def doAdd():
    global students
    #print("in do add")
    student = {}
    student["name"] = input("\tEnter student name:")
    student["modules"] = readModules()
    students.append(student)


def displayModules(modules):
    print("\t\tName \t\t Grade")
    for module in modules:
        print("\t\t{}\t\t{}".format(module["name"], module["grade"]))


def doView():
    print("All students")
    for student in students:
        print ("\t{}".format(student["name"]))
        displayModules(student["modules"])

#Main Program
choice = displayMenu()
while choice != "q":
    if choice == "a":
        doAdd()
    elif choice == "v":
        doView()
    elif choice == "q":
        pass
    else:
        print("Please select a, v or q.")
      
    choice = displayMenu()
    