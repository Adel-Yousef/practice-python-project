class Student:
    # Store name, list of grades
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        # Method to add a grade (0 to100 only). Invalid grades should raise an error.
        if grade >= 0 and grade <= 100:
            self.grades.append(grade)  # we are putting it at the end
        else:
            raise ValueError("Grade Must be between 0 and 100 inclusive")

    def average(self):
        # Method to calculate the average of grades. If no grades, return 0.
        if not self.grades:  # we can write if self.grades == False because inside the list is not a boolean valuse
            return 0
        
        total = 0
        for grade in self.grades:
            total += grade
        average = total / len(self.grades)
        return average


if __name__ == '__main__':
    Student_name = input("Enter the new student name: ")
    new_student = Student(Student_name)
    print(f"Welcome {new_student.name}")
    new_grade = input("Add grade to student: ")
    try:
        new_student.add_grade(int(new_grade))
    except ValueError as err:
        # To get the error messafe we included on line 12
        print(err)
