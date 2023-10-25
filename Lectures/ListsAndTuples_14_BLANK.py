# Class Activities (Lecture 14)

## lists
'''
0. Access a list of lists.
'''
recipe_ingredients = [["cheese", "chicken", "tomato sauce", "basil", "breadcrumbs"],
["chickpeas", "cucumber", "tzatziki", "tomatoes", "onion"],
["hamburger", "bun", "ketchup", "lettuce", "pickles", "mayo"],
["white beans", "celery", "diced tomatoes", "shallots", "broth"]]

print("QUESTION 0: ")
# Grab 'tzatziki' from recipe_ingredients using indexing




# Count the number of ingredients in the recipe in total
# Hint: Use len() to get the number of items in a list
#       Use for loop to iterate each sub-list to get #items and sum up




# If one's allergic to gluten, how to replace "bun" with "gluten-free bun"?




'''
1. Turn this while loop into a for loop.
'''
print("QUESTION 1: ")
my_list = ["music", "lego", "netflix", "tech", "tennis", "pets", "coding"]
# While loop version
i = 0
while i < len(my_list):
    print("I like " + my_list[i])
    i += 1

# write your code below
# For loop version




'''
2. Change the first item of my_list (from Q1) to be 'sun'
'''
print("QUESTION 2: ")
# write your code below




'''
3. Create a tuple, my_tuple, using the same items in my_list in Q1.
Then, change the first item to be 'ocean'. 
Does it work? Why?
'''
print("QUESTION 3: ")
# write your code below




'''
4. Create a shopping list: apple (count: 1), banana (count: 2), cherry (count: 3), dragonfruit (count 4)
    a. Construct a list of tuples, shopping_list, with each tuple containing a fruit above and its amount, say ("apple", 1).
    b. Print the fruit name whose amount is 2.
Hint: 
    Use a for loop to iterate shopping_list and only print the first item of a tuple, whose second item is 2.
'''
print("QUESTION 4: ")
# write your code below





