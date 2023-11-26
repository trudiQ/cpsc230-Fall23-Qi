# Class Activities (Lecture 20)

# In this exercise, you'll practice 
#   1. Create a class
#   2. Create a class instance
#   3. Add a method to a class
#   4. Access and modify instance variables
#   5. Access and modify class variables
#   6. Invoke a class method

# Exercise 1
# NOTE: You are adding code to the SAME class based on each question.
'''
E1. Define a class called 'Car' that has two instance variables 'brand' and 'model'
E2. Create a class instance named my_car with two arguments, where brand is Ford, model is Mustung
E3. Add a method named 'updateModel' within the class that modifies instance variable
    'model' with the new input argument named 'new_model'
E4: Create a class variable named 'wheels' and assign 4 to it
E5: Directly modify my_car's instance variable 'brand' to be 'Tesla'
E6: Modify my_car's instance variable 'model' to be 'Model S' using method 'updateModel'
'''
# write your code below
# E1
class Car:
    # E4
    wheels = 4
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    # E3
    def updateModel(self, new_model):
        self.model = new_model

# E2
my_car = Car(brand="Ford", model="Mustung")

# E5
my_car.brand = 'Tesla'

# E6
my_car.updateModel(new_model="Model S")


# Exercise 2
# NOTE: You are adding code the SAME class based on each question
'''
Q1: Create a new class named 'Book' that has two instance variables, 'title' and 'author'
Q2: Create an instance of the 'Book' class, my_book, with the title '1984' and author "George Orwell"
Q3: Add a method 'display_info' to the 'Book' class that prints out the book's title and author 
    in one message. Invoke 'display_info' after creating my_book to display the book's info.
Q4: Directly modify 'title' of 'my_book' instance to 'Animal Farm'. Invoke 'display_info' to 
    display the new book info.
Q5: Q5: Create a method 'updateTitle' within the class 'Book' that updates instance variable 'title'
    with 'new_title' - input argument of the method. Invoke the 'updateTitle' with argument 'Animal Farm'.
Q6: Add a class variable 'old_or_new' to the 'Book' and assign "old" to it. Create a new book, new_book, 
    to be George Orwell's 'Animal Farm' and update its class variable 'old_or_new' to be 'new'. 
    Print a message in this format "xxx's yyy is old/new".
'''
# write your code below
# Q1: Create a new class named 'Book' that has two instance variables, 'title' and 'author'
class Book:
    # Q6: Add a class variable 'old_or_new' to the 'Book' and assign "old" to it. 
    old_or_new = "old"
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # Q3: Add a method 'display_info' to the 'Book' class that prints out the book's title and author in one message.
    def display_info(self):
        print("Book title:", self.title, ", author:", self.author)

    # Q5: Create a method 'updateTitle' within the class 'Book' that updates instance variable 'title'
    #   with 'new_title' - input argument of the method.
    def updateTitle(self, new_title):
        self.title = new_title

# Q2: Create an instance of the 'Book' class, my_book, with the title '1984' and author "George Orwell"
my_book = Book(title="1984", author="George Orwell")

# Q3: Invoke 'display_info' after creating my_book to display the book's info.
my_book.display_info()

# Q4: Directly modify 'title' of 'my_book' instance to 'Animal Farm'. Invoke 'display_info' to 
#    display the new book info.
my_book.title = "Animal Farm"
my_book.display_info()

# Q5: Invoke the 'updateTitle' with argument 'Animal Farm'.
my_book.updateTitle(new_title="Animal Farm")

# Q6: Create a new book, new_book, to be George Orwell's 'Animal Farm'
#   and update its class variable 'old_or_new' to be 'new'
#  Print a message in this format: "xxx's yyy is old/new"
new_book = Book(title="Animal Farm", author="George Orwell")
new_book.old_or_new = "new"
print(new_book.author,"'s", new_book.title, "is", new_book.old_or_new)



