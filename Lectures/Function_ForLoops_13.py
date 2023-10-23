# Class Activities (Lecture 13)

## Practice functions with default arguments
'''
1. Write a function called 'simple_greeting' that takes a name and an age.
The age has a default value of 20.
The function should return a string in the format: "Hello, [name]. You are [age] years old." 
For example, when involking the function, you should see
    print(simple_greeting(name = "Alice")) ==>  "Hello, Alice. You are 20 years old."
    print(simple_greeting(name = "Bob", age = 30))  ==> "Hello, Bob. You are 30 years old."
'''
# write your code below
# define the funcition
def simple_greeting(name, age = "20"):
    message = "Hello, " + name + ". You are " + str(age) + " years old."
    return message

# call the function
print(simple_greeting(name="Alice"))
print(simple_greeting(name="Bob", age=30))

'''
2. Write a function 'triangle_area' that computes the area of a triangle 
using its base and height.
Both the base and height should have default values of 1.
When using the function, you should see
   print(triangle_area())  ===> 0.5
   print(triangle_area(base = 10, height = 5))  ===> 25.0
Hint: triangle_area = 0.5 * base * height
'''
# write your code below
# define the function
def triangle_area(base = 1, height = 1):
    area = 0.5 * base * height
    return area

print(triangle_area())
print(triangle_area(base=10, height=5))

'''
3. Write a function 'power' that accepts two inputs: 'base' and 'exponent'.
The exponent should have a default value of 0.5 (square root)
The function should return the result of 'base' to the power of 'exponent'
For example, 
    print(power(base = 2, exponent = 3))  ===> 8 (because 2 to the power of 3 is 8)
    print(power(base = 4))   ===> 2.0 (because 4 to the power of 0.5 is the square root of 4)
'''
# write your code below
# define the function
def power(base, exponent = 0.5):
    result = base ** exponent
    return result

# use the function
print(power(base=2, exponent=3))
print(power(base=4)) # default value of exponent is 0.5



## Practice functions with for loops
'''
4. Write a function 'upperCounter' that takes a string 'my_str' as input and 
count the number of characters that are uppercases.
Set 'HELICOPTER' as default argument for 'my_str'.
The function should return a string in the format: "[my_str] has 4 uppercase characters." 
For example, 
print(upperCounter())    ===> "HELICOPTER has 10 uppercase characters."
print(upperCounter(my_str = "A Beautiful Day!"))     ===> "Beautiful Day! has 2 uppercase characters."
Hint: Use for loop to iterate the input string and count the number of uppercases 
using string method ".isupper()" -> review Lecture 9: String Methods.
'''
# write your code below
# define the function
def upperCounter(my_str = "HELICOPTER"):
    counter = 0
    for c in my_str:
        if c.isupper():
            counter += 1
    message = my_str + " has " + str(counter) +" uppercase characters."
    return message

# use the function
print(upperCounter())
print(upperCounter(my_str="A Beautiful Day!"))

'''
5. Define a function 'sum_of_n' that takes an integer 'n'.
The function should return the sum of all integers from 1 to 'n', inclusive.
Default value of 'n' is 1.
For example,
    print(sum_of_n(n = 4))  ===> 10  (because 1 + 2 + 3 + 4 = 10)
Hint:
    use range() to generate the sequence of number from 1 to n.
    use a for loop to iterate the range() and add each number up.
'''
# write your code below
# define the function
def sum_of_n(n = 1):
    sequence_of_numbers = range(1, n + 1)
    sum = 0
    for i in sequence_of_numbers:
        sum += i
    return sum

# use the function
print(sum_of_n(n=4))