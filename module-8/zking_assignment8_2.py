import json

# Defining a class for a Student
class Student:
    def __init__(self, F_Name, L_Name, Student_ID, Email):
        self.F_Name = F_Name
        self.L_Name = L_Name
        self.Student_ID = Student_ID
        self.Email = Email
        
    def __repr__(self):
        return f"\nStudent(F_Name={self.F_Name}, L_Name={self.L_Name}, Student_ID={self.Student_ID}, Email={self.Email}\n"
    
    # Method to convert the Student object to a dictionary
    def to_dict(self):
        return {
            'F_Name': self.F_Name,
            'L_Name': self.L_Name,
            'Student_ID': self.Student_ID,
            'Email': self.Email
        }

# Define a function to load the JSON data into a list of Student objects
def load_students_from_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)  # Load the JSON data from the file
        
    # Map the data to Student instances
    students = [Student(student['F_Name'], student['L_Name'], student['Student_ID'], student['Email']) for student in data]
    return students

# Define a function to save the updated list of students back into the JSON file
def save_students_to_json(file_path, students):
    # Convert the list of Student objects to a list of dictionaries
    student_dicts = [student.to_dict() for student in students]
    
    # Save the updated data to the file
    with open(file_path, 'w') as f:
        json.dump(student_dicts, f, indent=4)

# Load the original students
students = load_students_from_json('student.json')

# Show the original list of students
print("This is the original Student list.")
print(students)

# Add a new student
new_student = Student('Zach', 'King', '12345', 'zachking@gmail.com')
students.append(new_student)

# Show the updated list of students
print("This is the updated Student list.")
print(students)

# Save the updated list of students back to the JSON file
save_students_to_json('student.json', students)
print("The student.json file has been updated.")