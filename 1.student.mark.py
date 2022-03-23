def get_num_Student():
    num_stu = int(input("Enter how many student: "))
    return num_stu

def stu_info(num_stu):
    students = []
    for i in range(num_stu):
        print(f"Enter student #{i+1}:")
        id = input("- ID: ")
        name = input("- Name: ")
        dob = input("- DoB: ")
        students.append({"Id": id, "Name": name, "DoB": dob})
    return students

def num_course():
    return int(input("Enter the number of courses: "))  

def course_info(num_course):
    courses = []
    for i in range(num_course):
        course_id = int(input(" * Course ID: "))
        course_name = input(" * Name of course: ")
        courses.append({"id": course_id, "name": course_name})
    return courses

def choose_course():
    return input("Choose a course(ID): ")

def course_mark(id, students):
    course_mark = []    
    i = 1
    for student in students:
        print(f"Enter student #{i} mark: ")
        print(f"-ID: {student['id']}, Name: {student['name']}, DoB: {student['dob']}")
        mark = int(input(" * Mark: "))
        course_mark.append({"c_id": id,"s_id": student['id'], "name": student['name'], "DoB": student['dob'], "Mark": mark})
        i += 1
    return course_mark

def course_list(courses):
    print("List of all Courses:")
    for course in courses:
        print(f"-ID: {course['course_id']}, Name: {course['course_name']}")

def student_list(students):
    print("Student List:")
    for student in students:
        print(f"-ID: {student['id']}, Name: {student['name']}, DoB: {student['dob']}")

def display_marks(id, course_mark):
    print(f"Listing course ID {id} marks:")
    for mark in course_mark:
        if(id == mark['c_id']):
            print(f"- Student ID: {mark['s_id']}, Name: {mark['name']}, DoB: {mark['DoB']}, Mark: {mark['Mark']}")

student_num = get_num_Student()
students = stu_info(student_num)
student_list(students)

course_num = num_course()
courses = course_info(course_num)
course_list(courses)

Choosen_course_ID = choose_course()
course_marks = course_mark(Choosen_course_ID, students)
display_marks(Choosen_course_ID,course_marks)