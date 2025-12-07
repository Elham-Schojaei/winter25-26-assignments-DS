# Assignment 1: Student Record Manager

## Objective
To build a basic Student Record Manager using a class structure to store, analyze, and retrieve student data. This assignment requires integrating concepts of variables, control flow, functions, loops, strings, and fundamental data structures (Lists, Dictionaries, Tuples, Sets), culminating in the use of Object-Oriented Programming (OOP).

## Part 1: The Student Class (OOP and Data Structures)
Create a Python class named Student.

    1. Class Attributes (Variables):

        - The Student class must have an initializer (__init__) that accepts the following arguments:
            - name (String)
            - student_id (String or Integer)
            - courses_and_grades (Dictionary, e.g., {'Math': 85, 'Science': 92, 'History': 78})

    2. Methods (Functions):
        - **get_average_grade(self)**:
            - Calculates and returns the average grade from the courses_and_grades dictionary.
        - **add_course_and_grade(self, course_name, grade)**:
            - Adds a new course and its corresponding grade to the student's courses_and_grades dictionary.
        - **get_honors_courses(self, threshold=90)**:
            - Uses a loop and conditional execution to find all courses where the grade is equal to or above the threshold (defaulting to 90).
            - Returns these high-performing course names as a List.
        - **get_unique_grades(self)**:
            - Returns a Set of all the unique grades the student has received.

## Part 2: The Manager Logic (Sequence Functions and Control Flow)
Outside of the Student class, implement the following steps:

    1. Initialize Data (Lists and Tuples):
        - Create a List named all_students to store instances (objects) of the Student class.
        - Create at least three Student objects with diverse data. For one student, ensure their initial courses are stored as a Tuple of (course, grade) pairs (e.g., [('Art', 95), ('PE', 88)]) and have your class initializer convert this into the required dictionary format upon creation.
    
    2. Apply Logic (Loops and Conditionals):
        - Use a Loop to iterate through the all_students list.
        - Inside the loop, use a Conditional Statement to check if a student's get_average_grade() is above 80.
        - If the average is above 80, print a formatted statement using String formatting (e.g., f-strings) saying: "[Student Name] has an excellent average of [Average Grade] and the following honor courses: [List of Honor Courses]".
        - If the average is 80 or below, call the add_course_and_grade method for that student, giving them a new course "Study Skills" with a grade of 100, and then print a statement confirming the addition.


class Student:
    def __init__(self, name, student_id, courses_and_grades):
        self.name = name
        self.student_id = student_id
        #self.courses_and_grades = courses_and_grades (removed for part 2)
        
        #This checks what type of data you passed in
        if isinstance(courses_and_grades, dict):
            self.courses_and_grades = courses_and_grades
        
        # If it is NOT a dictionary (e.g., a list of tuples), convert it to a dictionary
        else:
            self.courses_and_grades = dict(courses_and_grades)

    def get_average_grade(self):
        if len(self.courses_and_grades) == 0:
            return 0
        else:
            total = 0
            for value in self.courses_and_grades.values():
                total += value
            average = total / len(self.courses_and_grades)
            return average
        
    def add_course_and_grade(self, course_name, grade):
        #self.course_name = course_name
        #self.grade = grade
        #Do not create random new self.variables in other methods
        self.courses_and_grades[course_name] = grade
        return self.courses_and_grades
    
    def get_honors_courses(self, threshold=90):
        high_performing_courses = []
        #high_performing_courses = list() >> not working ??
        for key, value in self.courses_and_grades.items():
            if value >= threshold:
                high_performing_courses.append(key)

        return high_performing_courses
    
    def get_unique_grades(self):
        unique_grades = set(self.courses_and_grades.values())
        return unique_grades



all_students = []

student1 = Student( "Alice", "001", {"Math": 85, "Science": 92, "History": 78})

student2 = Student("Bob", "002", {"Math": 70, "English": 75, "Biology": 80})
                   
student3_courses = (("Art", 95), ("PE", 88))
student3 = Student( "Charlie", "003", student3_courses) 

all_students.append(student1)
all_students.append(student2)
all_students.append(student3)




for items in all_students:
    if items.get_average_grade() > 80:
        honor_courses = items.get_honors_courses()
        print(f"{items.name} has an excellent average of {items.get_average_grade()} and the following honors courses: {honor_courses}")    

    else:
        n = 0
        while items.get_average_grade() <= 80:
            items.add_course_and_grade(n, 100)
            n += 1

