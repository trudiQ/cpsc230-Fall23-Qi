# Class Activities (Lecture 7)

'''
0. What's wrong with this while loop and how can you fix it?
'''

#x = 1
#while x < 10:
#     print(x)

# solution
# this results in an infinte loop where x remains 1 the print 1 forever
x = 1
while x < 10:
     print(x)
     x += 1 # increment x's value to change the evaluation of the condition and end the loop

'''
1. Using a while loop, print out all the numbers between 1 and 10 (including)
'''
x = 1
while x <= 10:
    print(x)
    x += 1


'''
2. Using a while loop, print out all the numbers between 1 and 100 (including) that are
divisible by both 5 and 9.
Add comment for each line to explain the code
'''
x = 1
while x <= 100:
    if x % 5 == 0 and x % 9 == 0:
        print(x, "can be divided by both 5 and 9")
    x += 1

    

'''
3. Using a while loop, print out all the numbers between 1 and 100 (including) that are
divisible by both 5 and 9.
Exit the loop when the number is greater than 50.
Using break for this question.
Add comment for each line to explain the code
'''
x = 1
while x <= 100:
    if x % 5 == 0 and x % 9 == 0:
        print(x, "can be divided by both 5 and 9")
    if x > 50: # break when the number is greater than 50
        break
    x += 1


'''
4. Using a while loop, print out all the numbers between 1 and 10 (including) 
except for those which are divisiable by 3.
Using continue for this question.
Add comment for each line to explain the code
'''
x = 1
while x <= 10:
    if x % 3 == 0:
        x += 1
        continue
    print(x)
    x += 1