class Student:
    def __init__(self, student_id, name, grades):
        self.student_id = student_id
        self.name = name
        self.grades = grades

    def calculate_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Average Grade: {self.calculate_average_grade()}"

class Group:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        self.students = [s for s in self.students if s.student_id != student_id]

    def print_student_ratings(self):
        for student in sorted(self.students, key=lambda s: s.calculate_average_grade(), reverse=True):
            print(student)

    def __del__(self):
        print("Group instance deleted.")


if __name__ == "__main__":
    # Створення студентів
    student1 = Student(1, "Roma", [78, 92, 95])
    student2 = Student(2, "Ivan", [78, 92, 95])
    student3 = Student(3, "Danylo", [85, 88, 92])
    student4 = Student(4, "Andriy", [45, 79, 36])
    student5 = Student(5, "gidyla", [2, 3, 4])
    student6 = Student(6, "fff", [100, 100, 100])




    group = Group()


    group.add_student(student1)
    group.add_student(student2)
    group.add_student(student3)
    group.add_student(student4)
    group.add_student(student5)
    group.add_student(student6)



    print("Initial Student Ratings:")
    group.print_student_ratings()


    group.remove_student(2)
    print("\nAfter Removing Student 2 :")
    group.print_student_ratings()


    del group

