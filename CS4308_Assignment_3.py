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
            print("---------------------")
            print("Course Name: " + course.course_name)
            print("Course Number: " + course.course_number)
            print("Course Section: " + course.course_section)
            print("Course Term and Year: " + course.course_term_and_year)
            print("Number of Students: " + course.number_of_students)
            print("---------------------")
            
        
def main():

    menu_selection = None
    courses = []

    while menu_selection != 0:

        print("*** Course Catalog Creator ***")
        print("1 - Create a new course entry")
        print("2 - Change an existing course entry")
        print("3 - Print course catalog")
        print("0 - Quit")
        print("Please select a menu option: ")

        menu_selection = int(input())

        if menu_selection == 1:
                
            course_name = input("Please enter a course name: ")
            course_number = input("Please enter a course number: ")
            course_section = input("Please enter a course section: ")
            course_term_and_year = input("Please enter term and year: ")
            number_of_students = input("Please enter number of students: ")
            course = Course(course_name, course_number, course_section, course_term_and_year, number_of_students)                
            courses.append(course)

        elif menu_selection == 2:
            
            print("Please select the course you'd like to modify.")

            for index, course in enumerate(courses):
                print(index, course.course_name)

            user_course_choice = int(input())
            
            print("Which attribute would you like to change?")
            print("1 - Course Name")
            print("2 - Course Number")
            print("3 - Course Section")
            print("4 - Course Term and Year")
            print("5 - Number of Students")

            user_attribute_choice = int(input())

            if user_attribute_choice == 1:

                print("What would you like to change the course name to?")
                course_name_change = input()

                print("Changing course name...")
                
                courses[user_course_choice].set_course_name(course_name_change)


        
        elif menu_selection == 3:

            Course.print_courses(courses)
        
        else:
            print("Please enter a valid choice.")


if __name__ =="__main__":
    main()

