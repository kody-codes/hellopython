#This program defines a book object book object
# the objective is to create a book object and dispay its contents

class Books(object): # outlining book abject

    # the parameter self below refers to a newly created object.
    # It refers to an instance of of the method that was called in this case it Book().

    #Book has the following attributes
        # Author : String representing the authors name
        # Title: A string represent the title of the book
        # Pages: and integer representing the ammount of pages the object contains


    def __init__(self, author, title, pages): # defining object an passing in parameters ( author , title , pages)

        # The self.**** referes to a specific object created by the class
        # Ex: self.author refers to the attribute author placed inside the parameter.
        self.author = author
        self.title = title
        self.pages =pages



#creating an Book object call book1 and passing in its arttibutes
#NOTE the self parameter above in the def __int__() "REFERS TO BOOK1"

book1 = Books('Robert W. Sebesta', 'Concepts of Programming Languages 11/E', '761')

# Printing Attributes ao book1 example ouput is commented below each print statement.
print book1.author
# Robert W. Sebesta

print book1.title
# Concepts of Programming Languages 11/E

print book1.pages
#761