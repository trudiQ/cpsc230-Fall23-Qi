# Homework for Lectures 15 & 16
# Rename the file as HW_9_YOURNAME.py

# Complete at least 3 (code + report) out of 5 questions; they could be any 3.


'''
1. Can you manage a guest list based on the requirements below using list methods?
    a) Create a guest list of Alice, Bob, and Cory.
    b) Cory decided to bring a friend to the party. Use the append() method to add "David" to the list.
    c) You realized that you mistakenly added Bob, who won't be attending. 
        Use the remove() method to remove him from the list.
    d) Use the insert() method to add "Eva" to the list, making sure she is second in the invitation order.
    e) Pop the last person from the list, save this to a variable, and print a message saying they are on standby.
    f) Finally, print the sorted guest list based on REVERSED alphabetical order.
'''
# write your code below








'''
2. You have a list of dog breeds, use count() or index() method
    a) Find out how many Beagles are in the list and print the number.
    b) Find the position of the FIRST "Bulldog" in the list.
    c) Check the presence of "Dalmatian" in the list. If it's present, print its position; 
        otherwise, print "Dalmatian is not in the list".
'''
dog_breeds = ["Beagle", "Bulldog", "Chihuahua", "Beagle", "Poodle", "Beagle"]
# write your code below








'''
3. Imagine you are a data analyst at a film festival. You have ratings for a particular 
    movie from different critics as below.
    a) Calculate the total number of critics that reviewed the movie and print it.
    b) Find the highest and lowest rating given to the movie.
    c) Calculate the average rating of the movie.
    d) Create a NEW LIST of ratings sorted in ascending order and print it.
    e) The festival organizer wants to discard the lowest and highest rating to calculate the average again. 
        Remove those ratings, calculate the new average, and print it.
Hint: average = the sum of values / the number of values    
'''
ratings = [8.5, 9.0, 7.3, 9.3, 6.2, 10.0]
# write your code below









'''
4. Simulate a simple banking system with functions to deposit, withdraw, and check balance.
    a) Create a global variable account_balance initialized to 0.
    b) Write a function deposit(amount) that adds the amount to account_balance.
    c) Write a function withdraw(amount) that subtracts the amount from account_balance. 
        ENSURE that the withdrawal does not cause a negative balance. 
        If so, warn the user, and only allow them to withdraw the available amount (i.e., account_balance) 
        and set account_balance to be 0.
    e) Write a function check_balance() that prints the current balance.
    f) Perform a series of deposits and withdrawals, and check the balance as below. 
        Deposite $100 => Withdraw $50 => Withdraw $60 => Deposite $30 => Check_balance
       
NOTE: 
    Define all the required functions first and then call them one after another in f);
      MODIFY your code of Q1 for in-class exercise of Lecture 16
    EXPLAIN how account_balance has been changed for each action listed above, 
      leading to the final result in the report.
'''
# write your code below








'''
5. You are developing a hotel rating system where customers can give ratings out of 10.
The system calculates the average rating, total number of ratings, and a recommendation status.
    a) Write a function add_hotel_rating(ratings, new_rating) where ratings is a list of existing ratings 
        and new_rating is the new rating given by a new costomer. The function should add the new rating to the list 
        and return the updated average rating, total number of ratings, 
        and a recommendation status ("Recommended" if the average rating is above 7, otherwise "Not Recommended").
    b) Call the function with a sample list of ratings [7, 8.1] and a new rating, 6
        and store the returned values in 3 separate variables: average_rating, total_rating_number, recommendataion.
        Print out the updated hotel rating details with those 3 variables.
'''
# write your code below



