# Class Activities (Lecture 5)

'''
Ask the user to input which class they are here for. Store it in the varable class_name.
Use an if-else statement to check whether class_name is "cpsc230". 
If is, print "You are in the right classroom!".
Otherwise, print "You are in the wrong classroom!".
Use if-else statement.
'''
class_name = input()
if class_name == "cpsc230":
    print("You are in the right classroom!")
else:
    print("You are in the wrong classroom!")



'''
Ask the user to input a number and store it in the variable x.
Convert the value of x into an integer. 
Then check whether the number is even.
If yes, print "It's even" Othwise, print "It's not even."
Use if-else statement.
Hint: an even number can be exactly divided by 2, leaving a remainder of 0. 
'''
x = input()
x = int(x)
if x % 2 == 0:
    print("it's even")
else:
    print("it's not even")    




'''
Let's implement a simpler version of the game "Rock, Paper, Scissors" using conditionals.
* Rock crushes Scissors
* Scissors cuts Paper
* Paper covers Rock
1. Get two inputs from the user and stored them in variables player1_choice and player2_choice
2. Compare their choices:
    Assume player 1 always chooses 'Rock'
    When players 1 and 2 choose the same: print "It's a tie!"
    If player 2 chooses Scissors, print "Player 1 wins! Rock crushes Scissors!"
    If player 2 chooses Paper, print "Player 2 wins! Paper covers Rock!"
Use if-else and nested if statements. 
'''
# Option 1: if-else and nested if (under else)
player1_choice = "Rock"
player2_choice = input()
if player2_choice == "Rock": # if player1_choice == player2_choice:
    print("It's a tie!")
else: # Player2 could be "Paper", "Scissors", or anything
    if player2_choice == "Scissors":
        print("Player 1 wins! Rock crushes Scissors!")
    if player2_choice == "Paper":
        print("Player 2 wins! Paper covers Rock!")

# Option 2: if-else and nested if (under if)
player1_choice = "Rock"
player2_choice = input()
if player2_choice != "Rock": # Player2 could be "Paper", "Scissors", or anything
    if player2_choice == "Scissors":
        print("Player 1 wins! Rock crushes Scissors!")
    if player2_choice == "Paper":
        print("Player 2 wins! Paper covers Rock!")
else: # Player2 can only be "Rock"
    print("It's a tie!")

#---
# Can you spot the problem of the following code?
if player2_choice == "Rock":
    print("It's a tie!")
if player2_choice == "Scissors":
    print("Player 1 wins! Rock crushes Scissors!")
else: # Is 'Paper' the only option here? 
    print("player 2 wins! Paper covers Rock!")












