student_data = {}
course_data = {}


def display_menu():
    print("======================================")
    print(" Welcome to Student Management System")
    print("======================================")
    print("1. Add New Student")
    print("2. View Students")
    print("3. Add New Course")
    print("4. View Courses")
    print("5. Add Student Marks")
    print("6. Mark List")
    print("7. Quit")

def add_student(in4):
    num_std = int(input("How many Students: "))
    for i in range(1, num_std+1):
        print("Enter data for student #",i,": ")
        id = input("Enter student's ID: ")
        if not found(in4, id):
            name = input("Enter student's Name: ")
            dob = input("Enter student's Date of Birth: ")
            in4[id] = [name,dob]
        else:
            print(f"ID Existed!!!")

def student_list():
    print("{:15} | {:25} | {:25}".format("ID", "Name", "Date of Birth"))
    for key in student_data:
        print("{:15} | {:25} | {:25}".format(key, student_data[key][0], student_data[key][1]))


def add_course(in4):
    num_crs = int(input("How many Courses: "))
    for i in range(1, num_crs+1):
        print("Enter data for course #",i,": ")
        id = input("Enter course's ID: ")
        if not found(in4, id):
            name = input("Enter course's Name: ")
            in4[id] = [name]
        else:
            print(f"ID Existed!!!")

def course_list():
    print("{:15} | {:25}".format("ID", "Name")
    for key in course_data:
        print("{:15} | {:25}".format(key, course_data[key][0]))


def empty(dictionary):
    if len(dictionary) == 0:
        return True
    return False

def found(dictionary, id):
    if id in dictionary:
        return True
    return False




while True:
    display_menu()

    choice = input("Enter your choice: ")
    if choice == '1':
        add_student(in4=student_data)
    elif choice == '2':
        add_course(in4=course_data)
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    else:
        break