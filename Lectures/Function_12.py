# Class Activities (Lecture 12)
import random

'''
0. randint(a, b) is a function from a built-in library named random (see above import random)
that can be used to generate a random integer, N, between two integers, a and b, where a <= N <= b.
PART 1: Define a function, random_sum, that generates two random numbers between a and b (a < b) and return their sum.
PART 2: Invoke (use) the function to calculate the sum of two random numbers between 1 and 100 (inclusive)
and print the result.
'''
print("QUESTION 0 ---------------")
# example: generate a random number between 0 and 9 (inclusive)
x = random.randint(0, 9)
print(x)

# write your code below
# PART 1: define a function
def random_sum(a, b):
    # generate the first random number 
    num1 = random.randint(a, b)
    print("num1: ", num1)
    # generate the second random number
    num2 = random.randint(a, b)
    print("num2: ", num2)
    # sum
    sum = num1 + num2

    return sum

# PART 2: use the function
result = random_sum(1, 100)
print(result)


'''
1. Ask the user for their name, and print a welcome message to the user, e.g., "Welcome, Nicole!"
    PARK 1: Define a function that prints a welcome message using their input name.
    PARK 2: Invoke (use) the function and input the name user inputs to the function.
'''
print("QUESTION 1 ---------------")
# PART 1: define the function
def print_name(name):
    print("Welcome,", name, "!")

# PART 2: use the function
user_name = input("What's your name? ")
print_name(user_name)


'''
2. PART 1: Define a function that calculate a rectangle's perimeter based on
   its length and width as input. return its perimeter as output.
   Hint: rectangle's perimeter is 2 * (length + width). 
   PART 2: Invoke (use) the function your defined to calculate the perimeter 
   of a rectangle of length 5 and width 3 and print the result.
'''
print("QUESTION 2 ---------------")
# PART 1: define the function
def calculate_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter

# PART 2: use the function
my_length = 5
my_width = 3
my_perimeter = calculate_perimeter(length=my_length, width=my_width)
print("The perimeter of the rectangle is", my_perimeter)

'''
3. PART 1: Define a function returns True if the input number is greater than 10,
    and returns False otherwise.
   Part 2: Use the function to check the input argument of 16 and print out:
   "[argument] is greater than 10" or "[argument] is not greater than 10"
'''
print("QUESTION 3 ---------------")
# PART 1: define the function
def greater_than_10(number):
    if number > 10:
        return True
    else:
        return False

# PART 2: envoke the function
my_number = 16
result = greater_than_10(number=my_number)
if result == True:
    print(my_number, "is greater than 10")
else:
    print(my_number, "is not greater than 10")

