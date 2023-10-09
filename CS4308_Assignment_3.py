class Course(object):

    def __init__(self, course_name, course_number, course_section, course_term_and_year, number_of_students):
        self.course_name = course_name
        self.course_number = course_number
        self.course_section = course_section
        self.course_term_and_year = course_term_and_year
        self.number_of_students = number_of_students

    def set_course_name(self, course_name):
        self.course_name = course_name

    def set_course_number(self, course_number):
        self.course_number = course_number

    def set_course_section(self, course_section):
        self.course_section = course_section

    def set_course_term_and_year(self, course_term_and_year):
        self.course_term_and_year = course_term_and_year
    
    def set_number_of_students(self, number_of_students):
        self.number_of_students = number_of_students

    def print_course_name(self):
        print(self.course_name)

    def print_course_number(self):
        print(self.course_number)
    
    def print_course_section(self):
        print(self.course_section)
    
    def print_course_term_and_year(self):
        print(self.course_term_and_year)

    def print_number_of_students(self):
        print(self.number_of_students)

    @staticmethod
    def print_courses(courses):
        for course in courses:
            print("Course Name: ", course.course_name)
            print("Course Number: ", course.course_number)
            print("Course Section: ", course.course_section)
            print("Course Term and Year: ", course.course_term_and_year)
            print("Number of Students: ", course.number_of_students)
        

course1 = Course("English", "1101", "W01", "Fall 2023", "25")

course1.print_course_name()

course1.set_course_name("Mathematics")

course1.print_course_name()

courses=[]

course_name = input("Please enter a course name: ")
course_number = input("Please enter a course number: ")
course_section = input("Please enter a course section: ")
course_term_and_year = input("Please enter term and year: ")
number_of_students = input("Please enter number of students: ")
course1 = Course(course_name, course_number, course_section, course_term_and_year, number_of_students)





