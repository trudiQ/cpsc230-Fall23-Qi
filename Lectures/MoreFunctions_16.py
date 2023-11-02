# Class Activities (Lecture 16)

'''
1. Simulate a simple banking system with functions to deposit, withdraw, and check balance.
    a) Create a global variable account_balance initialized to 0.
    b) Write a function, named deposit(amount), that adds the input amount to account_balance.
    c) Write a function, named withdraw(), that only subtracts $10 from account_balance each time. 
    e) Write a function, named check_balance(), that prints the current account_balance.
    f) Perform a series of deposits and withdrawals, and check the balance as below. Print out the result.
        Deposite $100 => Withdraw $10 => Withdraw $10 => Deposite $30 => Check_balance
NOTE: Define all the required functions first and then call them one after another based on f)
'''
print("QUESTION 1: ")
# write your code below
# define all the functions here first
def deposite(amount):
    global account_balance
    account_balance += amount
    print("deposite", amount, "dollars") # optional

def withdraw():
    global account_balance
    account_balance -= 10
    print("withdraw 10 dollars") # optional

def check_balance():
    print("Account balance: ", account_balance)


# Perform a series of deposite, withdraw, and check balance
#   Deposite $100 => Withdraw $10 => Withdraw $10 => Deposite $30 => Check_balance
account_balance = 0
deposite(amount=100)
withdraw()
withdraw()
deposite(amount=30)
check_balance()


'''
2. Write a function, top_3_movies(), that asks the user to list their top 3 favorite movies 
separated by ','. Split the string into a list of the 3 movie titles (sub-strings).
Keep asking the user if they do not provide three movies titles.
Return those three movies titles.

Call your function top_3_movies(), and store those 3 movie titles using 3 variables, 
mov1, mov2, and mov3. Print out those 3 movie titles. 
'''
print("QUESTION 2: ")
# write your code below
def top_3_movies():
    while True:
        user_input = input("Please list three top movies, separated titles by commas: ")
        movie_titles = user_input.split(",")
        if len(movie_titles) == 3:
            break
    return movie_titles[0], movie_titles[1], movie_titles[2]

mov1, mov2, mov3 = top_3_movies()
print("I also like:", mov1, mov2, mov3)