# Class Activities (Lecture 6)

'''
** Update your previous code to use if-elif-else statements instead. **
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
'''
player1_choice = "Rock"
player2_choice = input()
if player2_choice == "Rock":
    print("it's a tie")
elif player2_choice == "Scissors":
    print("player1 wins")
elif player2_choice == "Paper":
    print("player2 wins")
else:
    print("Invalid input")





'''
Ask the user to input a number and store it in the variable x.
Convert the value of x into an integer. 
Check whether the number is even and greater than 17.
If yes, print "Yes!" Othwise, print "No."
Use if-else statement and a logical operator.
Hint: an even number can be exactly divided by 2, leaving a remainder of 0. 
'''
print("type a number please")
x = input() # or, you can directly do x = input("type a number please")
x = int(x)
if x % 2 == 0 and x > 17:
    print("Yes!")
else:
    print("No.")






