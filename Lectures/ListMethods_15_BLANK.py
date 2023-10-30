# Class Activities (Lecture 15)

# Outline
# 1 - 3 Exercise questions list operations
# 4 - 5 Exercise question on list methods
# 6 Exercise questions on list functions
# 7 - 8 More practice questions on list methods and functions

## List operations 
'''
1. List concatenation with +
TODO: Create a new list ['a','b','c','d','e','f'] 
        using the lists below
'''
print("QUESTION 1: ")
list0 = ['a', 'b', 'c']
list1 = ['d', 'e', 'f']



'''
2. List repetition with *
TODO: Repeat the list below 3 times
        you should see [1, 2, 3, 1, 2, 3, 1, 2, 3]
'''
print("QUESTION 2: ")
list2 = [1, 2, 3]



'''
3. List comparision with comparision operators
TODO: Are the following comparision expressions True or False?
        Print to see their results. Can you explain why?
'''
print("QUESTION 3: ")
[1, 2, 3] == [1, 2, 3]

[1, 2, 3, 4] > [1, 2, 3, 3]

print([1, 5, 2, 2, 2, 2] < [1, 6])


## List methods
'''
4. Given a list below representing a to-do list, 
    a) Use append() to add "Go for a walk" to the end of the list
    b) Use insert() to add "Buy groceries" as the SECOND item in the list
    c) Use pop() to remove AND print the LAST task in the list
    d) Use remove() to remove "Read a book" from the list
    e) Use sort() to sort the list alphabetically AND print the sorted list
'''
print("QUESTION 4: ")
tasks = ["Complete homework", "Read a book", "Write a report"]
# write your code below





'''
5. Given a list of colors below,
    a) Use count() to find and print how many times "red" appears in the list.
    b) Use index() to find and print the position of the FIRST "blue" in the list.
    c) Using a for-loop, find and print the indices of all occurrences of "red" in the list.
    d) Use count() to check for the presence of "yellow" in the list. 
        If it's there, print its position; if not, print a message saying "Yellow is not in the list".
'''
print("QUESTION 5: ")
colors = ["red", "blue", "green", "red", "blue", "red"]
# write your code below






## List functions
'''
6. Consider a list of temperatures (in Fahrenheit) for a week,
    a) Find and print the length of the temperatures list.
    b) Find and print the maximum and minimum temperatures of the week.
    c) Calculate and print the sum of the temperatures.
    d) Calculate and print the average temperature for the week using sum() and len().
    e) Sort and print the temperatures in ascending order.
    f) Sort and print temperatures in descending order.
'''
print("QUESTION 6: ")
temperatures = [72, 75, 68, 79, 71, 73, 78]
# write your code below





# More practice questions on list methods and list functions

'''
7. Start with the following list of numbers:
    1) Use the append() method to add the number 5 to the list.
    2) Use the insert() method to insert 15 at the beginning of the list.
    3) Use the pop() method to remove and print the second number in the list.
    4) Use the remove() method to remove the number 7 from the list.
    5) Use the sort() method to sort the list in descending order and print the result.
'''
print("QUESTION 7: ")
numbers = [10, 3, 7, 2, 8]
# write your code below




'''
8. You work for an online marketplace, and you have collected customer review scores for a popular product:
    1) Calculate the total number of reviews.
    2) Find the highest and lowest review scores.
    3) Calculate the average review score.
    4) Sort and print the review scores in both ascending and descending order.
    5) The product manager decides to filter out the lowest score for a better understanding of the product's performance. 
        Remove the lowest score, recalculate the average, and print it.
'''
print("QUESTION 8: ")
reviews = [4.5, 3.8, 4.2, 4.7, 3.9, 4.0]
# write your code below







