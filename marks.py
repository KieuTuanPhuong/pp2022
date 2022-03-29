class Mark:
    def __init__(self, id, name, mark):
        self.id = id
        self.name = name
        self.mark = mark


class mark_Info:
    def __init__(self):
        self.marks = {}

    def select_course(self, courses):
        choice = input("Enter course id: ")
        for i in range(len(courses)):
            if choice == courses[i].id:
                return courses[i]
        return "404 Not Found!"

    def enter_mark(self, courses, students):
        select_course = self.select_course(courses)
        if select_course == "404 Not Found!":
            print("Course not found!")
        else:
            mark_list = []
            n = 0
            for i in range(len(students)):
                mark = input(f"Student ID: {students[i].id} - Student Name: {students[i].name}\nEnter mark: ")
                student_mark = Mark(students[i].id, students[i].name, mark)
                mark_list.append(student_mark)
                n = n + 1
            self.marks[select_course.id] = mark_list
            print(f"{n} students added")
            return self.marks

    def display_mark(self, courses, students):
        select_course = self.select_course(courses)
        course_mark = self.marks[select_course.id]
        if select_course == "404 Not Found!":
            print("Course not found!")
        else:
            print(f"{select_course.name} mark sheet")
            print("{:3} | {:10} | {:20} | {:10}".format("No.", "ID", "Name", "Mark"))
            for i in range(len(students)):
                print("{:3} | {:10} | {:20} | {:10} ".format(str(i+1), course_mark[i].id, course_mark[i].name, course_mark[i].mark))