# Class Activities (Lecture 8)

'''
1. Create a string 'Hello World!' and store it to a variable named str1.
    a. Print out charater 'H' in this string using index.
    b. Slice this string to get 'ello' and assign it to another variable named str2 and print it.
'''
str1 = 'Hello World!'
print(str1[0])
str2 = str1[1:5]
print(str2)



'''
2. Use operator in to check if 'Hello World!' contains a space, i.e., ' '
    if yes, print out "Yes, there is a space."; otherwise "No space."
'''
str1 = 'Hello World!'
# check '!'
if '!' in str1:
    print("Yes, there is a '!'")
else:
    print("No '!'")

# check ' '
if ' ' in str1:
    print("Yes, there is a space")
else:
    print("No space")



'''
3. Ask the user to input two words and store them into two variables, x and y.
Use addition (+) to add these two variables together and assign the result back to x.
print out x in this format: "Here is the combined word: [result]" where result is the value of x.
'''
x = input("give a word: ")
y = input("give another word: ")
x += y
print("Here is the combined word:", x)



'''
4. Write a while loop to ask the user to input one character (a letter, a number, or a symbol) at a time.
Print whatever they just typed. If they typed nothing and hit enter (they created an empty string), 
print "Nothing was typed. Exit now. " and end the loop using break.
'''
while True:
    x = input("Please type a character: ")
    if x != "":
        print(x)
    else:
        print("Nothing was typed. Exit now.")
        break






