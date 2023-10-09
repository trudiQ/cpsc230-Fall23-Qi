# Class Activities (Lecture 10)

'''
1. Use a for loop and range() to create integers from 0 to 5 and print them out.
'''
print("QUESTION 1:")
# write your code below
for i in range(0, 6):
    print(i)



'''
2. Use a for loop and range() to create integers from 0 to 5 and print them out.
Use a loop variable to count iteration number and print it out after the for loop.
'''
print("QUESTION 2:")
# write your code below
count = 0
for i in range(0, 6):
    print(i)
    count += 1
print("Total iteration number:", count)


'''
3. Put the names of your groupmates in a list (example below), then use a for
loop to print out "You're a valuable member of group [group number], [Name]"
for each name.
'''
print("QUESTION 3:")
# write your code below
names = ['Bill', 'Nicole', "John"] # replace with your groupmates names in the list
for name in names:
    print("You're a valuable member of group 1,", name)

'''
4. Use a for loop to iterate a list of temperatures (Celsius), use variable num_neg 
    to count the number of below-freezing (< 0) temperatures, and print the result.
'''
print("QUESTION 4:")
temperatures = [30, 20, 2, -5, -15, -8, -1, 0, 5, 35]
num_neg = 0
# write your code below
for temp in temperatures:
    if temp < 0:
        num_neg += 1
print("There are", num_neg, "below-freezing temperatures.")


'''
5. Ask the user to input two words of the SAME LENGTH. Using a for loop, count
how many corresponding letters are the same in the two strings. 
For example in spam and span, 3 of the letters (s,p,a) are the same. 
In the words bitter and better,5 of the letters are the same. 
Print out a message telling the user how many letters are the same.
Hint: Iterate each pair of characters of the same index in both strings and compare.
'''
print("QUESTION 5: ")
# write your code below
word1 = input("Please type the FIRST word: ")
word2 = input("Please type the SECOND word: ")
length1 = len(word1)
length2 = len(word2)
count_same_letters = 0
if length1 == length2:
    for i in range(length1):
        if word1[i] == word2[i]:
            count_same_letters += 1
    print(count_same_letters, "of the letter are the same.")
else:
    print("Please type two words of the SAME LENGTH!")



