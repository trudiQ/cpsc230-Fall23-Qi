# Class Activities (Lecture 9)

'''
1. Ask the user to input a random word, assig it to my_string.
First, check if my_string is all uppercased. 
If yes, print out "Good, all're uppercased!".
Otherwise, convert my_string to all uppercase and print out the result.
'''
print("QUESTION 1")
my_string = input("Please input a word: ")
if my_string.isupper():
    print("Good, all're uppercased!")
else:
    new_string = my_string.upper()
    print(new_string)

'''
2. Replace all occurrences of "coffee" with "hot chocolate" and "programmer" 
with "coder". Print out the result.
'''
print("QUESTION 2: ")
paragraph = """In the town of Coderville, every programmer loved to drink coffee; 
coffee gave them the energy to code late into the night. 
However, some programmers preferred tea over coffee."""

new_paragraph_1 = paragraph.replace("coffee", "hot chocolate")
new_paragraph_2 = new_paragraph_1.replace("programmer", "coder")
print(new_paragraph_2)


'''
3. Ask the user to type at least two words separated spaces, store the input to a variable named my_string.
    a. Check if the first character is capitalized, print out "[user input]'s first character is capitalized".
    b. Check if the first character is a number, , print out "[user input]'s first character is a number".
    c. Print how many words in my_string
        Hint: Split my_strings by space and print the length of the list of tokens.
'''
print("QUESTION 3: ")
my_string = input("Please enter at least two words: ")
# a.
if my_string[0].isupper():
    print("first character is capatlized.")
else:
    print("first character is not capitalized.")
# b.
if my_string[0].isdigit():
    print("first character is a number.")
else:
    print("first character is not a number")
# c.
my_list = my_string.split()
print("there are", len(my_list), "words.")
