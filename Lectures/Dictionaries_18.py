# Class Activities (Lecture 18)

# iterate over keys using keys()
'''
Q1: Given a dictionary of stock prices below, prints out all the stock names in uppercase.
Expected Output:
APPLE
MICROSOFT
AMAZON
NOTE: Use for loop to iterate each key and uppercase it (check Lecture 9)
'''
print("QUESTION 1: ")
stocks = {"Apple": 150, "Microsoft": 210, "Amazon": 3100}
# write your code below
for key in stocks.keys():
    key.upper()
    print(key)



# iterate over values using values()
'''
Q2: Given a grocery cart below, write some codee to calculate the total price of all items in it - the sum of
all the values in the dictionary, where the fruit name is the key and the value is the price per item. 
Assume each fruit has a quantity of one.
Expected Output:
Total cost is: $X.XX
Hint: Use a for loop to iterate all the values in the dictionary, and add each value to a counter 
to get the sum of all the values.
'''
print("QUESTION 2:")
cart = {"banana": 0.99, "apple": 0.50, "peach": 1.25}
# write your code below
total_cost = 0
for value in cart.values():
    total_cost += value
print("Total cost is:", total_cost)




# iterate over items using items()
'''
Q3: Following Q1, iterate each item in stocks and print out the company name whose stock price is over $500
'''
print("QUESTION 3:")
# write your code below
for key, value in stocks.items():
    if value > 500:
        print(key)


'''
Q4: Follow Q2, due to inflation, each the price of each fruit in your grocery cart, cart, has been increased 
    with banana by 10%, apple by 15%, and peach by 20%. Re-calculate the total cost.
Expected Output:
Updated total cost is: $X.XX
'''
print("QUESTION 4:")
# write your code below
updated_total_cost = 0
for key, value in cart.items():
    if key == "banana":
        updated_total_cost += value * (1 + 0.1)
    elif key == "apple":
        updated_total_cost += value * (1 + 0.15)
    elif key == "peach":
        updated_total_cost += value * (1 + 0.2)
print("Updated total cost is:", updated_total_cost)
        


'''
Q5: Given two lists, one with student names and the other with their respective grades, 
    create a dictionary, named student_record, that maps each student to their grade.
    Print out the dictionary.

Expected Dictionary Output:
{"Emma": "A", "Olivia": "B", "Noah":"C", "Liam":"A"}

Hint: 
    - Create student_record as an empty dictionary first
    - Use a for loop with range(0, len(names)) to iterate items in both lists, names and grades, by the indices
    - First list, names, contains keys, and second list, grades, contain values respectively
    - Add each pair of (key, value) to the dictionary, student_record.
'''
print("QUESTION 5:")
names = ["Emma", "Olivia", "Noah", "Liam"]
grades = ["A", "B", "C", "A"]
# write your code
student_record = {} # create an empty dictionary
for i in range(0, len(names)):
    name = names[i]
    grade = grades[i]
    student_record[name] = grade # or, student_record.update({name, grade})
    print(i, "added", name, grade) # this is not required, just show you what iteration looks like
print(student_record)