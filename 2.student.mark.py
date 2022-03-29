
from courses import course_Info
from marks import mark_Info
from students import student_Info
from students import student_Info
from courses import course_Info
from marks import mark_Info

end = False
std = student_Info()
crs = course_Info()
mrk = mark_Info()
Students = []
Courses = []

print("Choose an option:")
while not end:
    print("==============================")
    print("1. Add Student")
    print("2. Add Course")
    print("3. Display Student List")
    print("4. Display Mark List")
    print("5. Edit Student Mark")
    print("6. Mark by Course")
    print("0. EXIT")
    choice = input("Enter your choice: ")
    if choice == "1":
        Students = std.std_info()
    elif choice == "2":
        Courses = crs.add_course()
    elif choice == "3":
        Students = std.display_std()
    elif choice == "4":
        Courses = crs.Display_course()
    elif choice == "5":
        mark_Info.enter_mark(Courses, Students)
    elif choice == "6":
        mark_Info.display_mark(Courses, Students)
    elif choice == "0":
        end = True
    else:
        print(f"{choice} is an invalid input!")
    
    
