class student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

class student_Info:
    def __init__(self):
        self.num = 0
        self.stds = []

    def std_num(self):
        self.num = int(input("Enter number of Student: "))
        return self.num

    def std_info(self):
        for i in range(self.std_num()):
            id = input("ID: ")
            name = input("Name: ")
            dob = input("Date of Birth: ")
            std = student(id, name, dob)
            self.stds.append(std)       
        print(f"{self.num} students added")
        return self.stds

    def display_std(self):
        print("{:3} | {:10} | {:20} | {:20}".format("No.", "ID", "Name", "Date of Birth"))
        for i in range(len(self.stds)):
            print("{:3} | {:10} | {:20} | {:20}".format(str(i+1), self.stds[i].id, self.stds[i].name, self.stds[i].dob))
    