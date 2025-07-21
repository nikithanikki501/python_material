'''
Functions - Two Types
 1. Inbuilt functions - Functions provided by Python. Can be readily used. 
 2. User Defined functions / Custom functions - We write it because it is not readily available.
     a. Named Functions - Can be reused.
     b. Nameless Functions - Cannot be reused. Also called as lambda functions.

Functions can have arguments or need not have arguments:
    1. Zero arguments
    2. Multiple arguments
    3. Variable arguments
    4. Variable Keyword arguments
'''           

# Example for advantages of functions
# Imagine there are 100 lines of code created based on a requirement without using functions.

# Print the string "If you have guts, catch me shekawat" to the console.
print("If you have guts, catch me shekawat") 

# Print the string "If you have guts, catch me shekawat" to the console.
print("If you have guts, catch me shekawat") 

# Print the string "If you have guts, catch me shekawat" to the console.
print("If you have guts, catch me shekawat") 

# Print the string "If you have guts, catch me shekawat" to the console.
print("If you have guts, catch me shekawat") 

# Create a user defined function with any name & reuse that name instead of typing lengthy sentences. 
def sayHello(): # functions start with keyword 'def'. () -> Zero arguments
    print('If you have guts, catch me shekawat') # Block belonging to the function

sayHello() # reuse the function name then function will be called and output is displayed

# Simple function 
def hello(name, age, sal): # function with '3' arguments                
    print("hi", name, "your age is:", age, "your salary is:", sal)

# Call the hello function with arguments "Shekawat", 25, and 50000.
hello("Shekawat", 25, 50000)

hello("Shekawat", 25) # function 'hello' has 3 arguments but we are giving only '2' & hence the error

# Formal and actual arguments

# Function definition
def add(a, b):
    return a + b 

# function call
add(2, 3) # a= 2 & b = 3


# Formal arguments 'a' & 'b' are identifiers used in the function definition 
# to represent corresponding actual arguments.

# Actual arguments are values (or variables / expressions) that are used inside
# the parentheses of a function call.

# Positional arguments
def rectangleArea(width, height):
    return width * height # Calculate the area of a rectangle using width and height.

# Print the area of a rectangle with width 1 and height 2.
print(rectangleArea(width = 1, height = 2))

def printMax(a, b): # has two arguments 'a' & 'b'
    if a > b: # Check if a is greater than b.
        print(a, 'is maximum') # Print a is maximum if it is greater.
    elif a == b: # Check if a is equal to b.
        print(a, 'is equal to', b) # Print a is equal to b if they are equal.
    else:
        print(b, 'is maximum') # Print b is maximum if a is not greater than b.

# Call printMax function with arguments 3 and 4.
printMax(3, 4) # a = 3 & b = 4

def say(message, times = 1): # two arguments - message, times
    print(message * times) # Print the message times the specified number of times.

# Call say function with the message 'Hello' and default times value of 1.
say('Hello') 
'''Argument 'message' = Hello & despite not giving 'times' argument, 
it will run without error because 'times = 1' is already defined in the 
function we created '''

# Call say function with the message 'World ' and times value of 5.
say('World ', 5) # Argument 'message' = World, 'times' = 5; This will replace the argument 'times = 1' defined in the function.


def func(a, b = 5, c = 10): # This function has '3' arguments 'a', 'b', 'c'
    print('a is', a, 'and b is', b, 'and c is', c)  # Print values of a, b, and c.

# Call func with arguments 3 and 7. a = 3, b = 7, c = 10
func(3, 7)

# Call func with arguments 25 and using default value for b, and explicitly setting c to 24.
func(25, c = 24)

# Call func with argument a set to 100, and explicitly setting c to 50, using default value for b.
func(c = 50, a = 100)


# Variable / Multiple arguments rather than hard coding the number of arguments
# *arg can be used for having variable number of arguments 
def myFun(*argv): # *argv will allow variable/multiple arguments
    for i in argv: # Iterate through all arguments passed to the function.
        print(i)  # Print each argument.

# Call myFun with multiple arguments.
myFun('Hello', 'Welcome', 'to', '360digitmg', 360)  

# Use **kwargs to pass the variable "keyword arguments" to the function 
def intro(**data): # Remember dictionary - Key & Value pairs
    print("\n Data type of argument:", type(data))
    for key, value in data.items(): # Iterate through the key-value pairs in the data dictionary.
        print("{} is {}".format(key, value))    # Print each key-value pair.

# Call 'intro' function with a dictionary of key-value pairs as arguments.
intro(Firstname = "Bahu", Lastname = "Bali", Age = 25, Phone = 9654321123) # '4' items (key-value pairs)
intro(Firstname = "Pushpa", Lastname = "Raj", Email = "pushparaj@nomail.com", Country = "Seshachalam Hills", Age = 23, Phone = 9876543210) # '6' items (key-value pairs)


# Defining a function with fixed argument, variable arguments & variable keyword arguments
def total(initial, *numbers, **keywords):
    count = initial  # Initialize count with the initial value.
    # Iterate through the positional arguments (numbers) and add them to count.
    for number in numbers:
        count += number
    # Iterate through the keyword arguments (keywords) and add their values to count.
    for item in keywords:
        count += keywords[item] 
    # Return the total count.
    return count

# Call the total function with initial value 10, positional arguments 1, 2, 3, and keyword arguments vegetables = 50, fruits = 100.
print(total(10, 1, 2, 3, vegetables = 50, fruits = 100))

## Function call stack
### locals(), globals()
x = 5  # Define a global variable x with value 5.

def new():
    print('number is', x) # Access the global variable x and print its value.

# Call the new function.
new()

# Print the global variable x outside the function.
print(x)

x = 5  # Define a global variable x with value 5.

def new():
    x = 10 # Define a local variable x with value 10.
    print('number is', x) # Print the local variable x.

# Call the new function.
new()

# Print the global variable x outside the function.
print(x)


age = 23 # Age Global variable
name = "Gabbar" # Name Global Variable
places = ["Nagpur", "Mumbai", "Pune"] # Places Global Variable

def local(): # Function declaration  
    age = 1 # Age Local Variable
    name = 'Mogambo' # Name Local Variable
    print("%s is %i years old and lives in %s." % (name, age, places[0])) # Function Definition for Local Variable
    # In the above line of code name and age variables are Local and place is Global Variable 
    return

# Run these three lines of code at one go
local() # Function calls Local() Variables
print("##############")
print("%s is %i years old and lives in %s." % (name, age, places[2])) # Calling definition for Global Variable


## Declaring global variable within function
x = 5

def new():
    global x  # Declare x as global within the function.
    x = 10    # Assign a new value to the global variable x.
    print('number is', x)

# Call the new function, which modifies the global variable x.
new()

# Print the modified value of the global variable x.
print(x)

# Regular way of defining function vs Recursive Function demonstration
# Regular way of defining function
def fact(N):
    if N < 0:    # Check if the input N is negative.
        print("Input the positive number")  # If N is negative, print an error message.
    elif N == 0: # Check if the input N is zero.
        print(f'Factorial of {N}! is {1}') # If N is zero, print the factorial of 0 which is 1.
    else: # If N is positive, initialize the variable fact to 1.
        fact = 1  
        for i in range(1, N + 1): # Iterate through the range from 1 to N (inclusive).
            fact *= i  # Multiply fact by each value in the range to calculate the factorial.
        print(f'Factorial of {N}! is {fact}') # Print the factorial of N.

# Call the fact function with argument 5.
fact(5)

# Recursive function - Calling function within a function.
def fact(N):
    if N < 0: # Check if the input N is negative.
        print("Input the positive number") # If N is negative, print an error message.
    elif N == 0: # Check if the input N is zero.
        print(f'Factorial of {N}! is {1}') # If N is zero, print the factorial of 0 which is 1.
    elif N == 1: # Check if the input N is 1.
        return 1  # If N is 1, return 1 (base case for recursion).
    else:
        # If N is greater than 1, recursively call the fact function with N-1 and multiply the result by N.
        return (N * fact(N-1))

# Call the fact function with argument 5.
fact(5)


# List Comprehensions and Readability 
# Build a list of Unicode codepoints from a string in ordinary way 
# Define a string containing various currency symbols.
symbols = '$¢£¥€¤'

# Initialize an empty list to store Unicode values of the symbols.
codes = []

# Iterate over each symbol in the symbols string.
for symbol in symbols:
    # Append the Unicode value of the current symbol to the codes list using ord() function.
    codes.append(ord(symbol))

# Print the list of Unicode values.
print(codes)


# Alternative way to perform the above Unicode conversion using list comprehension.
symbols = '$¢£¥€¤' # Define the symbols string again.

# Use list comprehension to iterate over each symbol in the symbols string and convert them to Unicode.
codes = [ord(symbol) for symbol in symbols]

# Print the list of Unicode values.
print(codes)

# Create a new list containing odd numbers from 0 to 11 using list comprehension.
new_list = [i for i in range(12) if i % 2 == 1]

# Print the new list.
print(new_list)


## Dictionary Comprehension

# Let us see how the same problem can be solved using a for loop and dictionary comprehension
# Define a range of numbers from 0 to 9.
numbers = list(range(10))

# Print the range object.
print(numbers)

# Initialize an empty dictionary to store square values of even numbers.
new_dict_for = {}

# Add values to 'new_dict_for' using 'for' loop.
for n in numbers:
    if n % 2 == 0:  # Check if the current number is even.
        # Calculate the square of the current number and store it as value in the dictionary.
        new_dict_for[n] = n ** 2

# Print the resulting dictionary.
print(new_dict_for)

# Use dictionary comprehension to create a dictionary with square values of even numbers.
new_dict_comp = {n: n**2 for n in numbers if n % 2 == 0}

# Print the resulting dictionary created using dictionary comprehension.
print(new_dict_comp)


# Another example using dictionary comprehension.
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5} # Define a dictionary.

# Create a new dictionary where keys are doubled and values are doubled.
dict1_keys = {k * 2: v * 2 for (k, v) in dict1.items()}

# Print the resulting dictionary.
print(dict1_keys)


## Zip and Unzip
# Python code to demonstrate the working of zip() 
name = ["Shakaal", "Gabbar", "Pathan", "Prem"] # Define a list containing names.
roll_no = [4, 1, 3, 2] # Define a list containing roll numbers.
marks = [40, 50, 60, 70] # Define a list containing marks.

# Using zip() to map values 
mapped = zip(name, roll_no, marks) 
print(mapped)
  
# Converting values to print as set 
mapped = set(mapped)  
print("The zipped result is : ", mapped) # Printing resultant values 

# Unzipping values 
# Unzip the tuples obtained from zip() and assign them to separate lists.
namez, roll_noz, marksz = zip(*mapped) 

# Run all the following lines of code with 'print'at one go
print("The unzipped result: \n") # Print a header for the unzipped result.
print("The name list is : ", end = "") 
print(namez) 
print("The roll_no list is : ", end = "") 
print(roll_noz)   
print("The marks list is : ", end = "") 
print(marksz)

# Built-in Functions
# Sort
animals = ['dog', 'cat', 'cow', 'sheep', 'goat', 'elephant']
sorted(animals) # Ascending order with alphabet (lexicographical)
sorted(animals, reverse = True) # Descending order with alphabet by including parameter "reverse = True"

# Descending order with respect to length of the character
sorted(animals, key = len, reverse = True) # 'key' & 'reverse' parameters are also included in the function 'sorted'

# Ascending order with respect to length of the character 
sorted(animals, key = len) # default value of 'reverse' parameter is False

# Object 'animals' in memory is not updated
sorted(animals) # on console output you see items sorted based on alphabets (lexicographical technique)

# Built-in function for sort
animals.sort() # it will update memory as well alongside sorting

# sorted function will not update memory & .sort() will update memory 

# Augmented Assignments with Sequences
# Explanation of mutability and immutability for list and tuple using memory location identity
# Augumented assignment operators with *=

l = [1, 2, 3]
print(id(l), l) # id of lists 

# ID of list will not change, it will just append the values to the same ID
l *= 2 # Equal to l*2
print(id(l), l)

# Augumented assignment operators with *=
t = (1, 2, 3)
print(id(t), t)
# ID of the tuple will change instead of appending the values to the same ID 
t *= 2
print(id(t), t) 

# Handling Missing Keys
d = {'a' : 1, 'b' : 2} # Initializing Dictionary
print(d['a'])

print("The Value associated with 'c' is : ") # trying to output value of absent key
print(d['c'])

# We need to handle these kind of errors
import collections as cl # importing "collections" for default dict

# Declaring defaultdict
# Sets default value 'key Not found' to absent keys
defd = cl.defaultdict(lambda : 'key is Not Available')

defd['a'] = 1 # initializing values
defd['b'] = 2 # initializing values

print("The value of 'a' is : ", end = "") # end = "" will ensure that next line output also appears in this same line
print(defd['a'])

print("The value of 'c' is : ", end = "")
print(defd['c'])


# Lambda Functions are nameless functions, which cannot be reused
# Defining the lambda function 
s = lambda x: x * x # def is not used to define this function
s(12)

# map()
# map(function,  iterable) # iterable is any object/variable whose values can be iterated
# Define a list containing integers.
val = [1, 2, 3, 4, 5, 6] # val is iterable object

# Using map() to double each element in the list and convert the result to a list.
doubled = list(map(lambda x: x * 2, val))
print(doubled)

# Using map() to convert each element in the list to a string and convert the result to a list.
converted_to_str = list(map(str, val))
print(converted_to_str)


# Using filter() to filter out odd numbers from the list and convert the result to a list.
val1 = [1, 2, 3, 4, 5, 6]
filtered_odd = list(filter(lambda x: x % 2, val1)) # val1 is iterable object
print(filtered_odd)

# Using filter() to filter out numbers greater than 50 from a list generated using range() and convert the result to a list.
filtered_greater_than_50 = list(filter(lambda x: x > 50, list(range(1, 100))))
print(filtered_greater_than_50)


# Using reduce() to find the product of all elements in the list.
from functools import reduce # library is "functools" and module is "reduce"
val = [1, 2, 3, 4, 5, 6]
product = reduce(lambda x, y: x * y, val) # val is iterable object
print(product)  # 1 * 2 * 3 * 4 * 5 * 6

# Using reduce() to find the sum of all elements in a list generated using range().
sum_of_elements = reduce(lambda x, y: x + y, list(range(1, 100)))
print(sum_of_elements)  # 1 + 2 + 3 + 4 + 5 + ........

# Print documentation for reduce() function.
dir(reduce)
help(reduce)

## Loop vs Comprehension vs Map (lambda function)

# Original list
list1 = [1, 2, 3, 4, 5]

# Using a loop to calculate squares
squares1 = [] # create an empty list called squares1

for i in list1:
    squares1.append(i ** 2) 
squares1

# Using list comprehension to calculate squares
squares2 = [i ** 2 for i in list1]
squares2

# Using map and lambda function to calculate squares
squares3 = list(map(lambda x: x ** 2, list1))
squares3

# Printing the results
squares1, squares2, squares3


# Iterators
# Iterator is an object which allows a programmer to traverse through all the 
# elements of a collection, regardless of its specific implementation.

# Define a list of names.
names = ["Shakaal", "Gabbar", "Pathan", "Prem"]

# Print the list of names.
print(names)  # iterable

# Convert the list into an iterator using the __iter__() method.
new_list = names.__iter__()
print(new_list)

# Print documentation for the iterator object.
help(new_list)

# Iterate over the iterator and print each element.
for obj in new_list:
  print(obj)

# Attempting to print an element directly from the list raises an error because lists are iterables, not iterators.
names = ["Shakaal", "Gabbar", "Pathan", "Prem"]
names   # iterable
print(next(names))  # Raises TypeError

# Attempting to print an element directly from the iterator works.
new_list = names.__iter__()
print(next(new_list))  # Prints the first element of the iterator
print(next(new_list))  # Print the first element of the iterator

# Convert the list into an iterator using the iter() function.
new_list = iter(names)
print(next(new_list))  # Print the first element of the iterator
print(next(new_list))  # Print the next element from the iterator.
print(next(new_list))  # Print the next element from the iterator.
print(next(new_list))  # Print the next element from the iterator.


# Why use iterator?

# An "iterable" is an object that has an __iter__ method which returns an # 
# iterator, or defines a __getitem__ method that can take sequential indexes 
# starting from zero. So an iterable is an object that you can get an iterator.

# An "iterator" is an object with a next (Python 2) or __next__ (Python 3) method.

# Whenever you use a 'for' loop, or map, or a list comprehension, etc., in 
# Python, the next method is called automatically to get each item from the 
# iterator, thus going through the process of iteration.

# Create a list of numbers from 0 to 999999.
names = [i for i in range(1000000)]

# Convert the list into an iterator.
new_list = iter(names)

# Import the sys module to access system-related information.
import sys

# Print the size of the 'names' variable in bytes.
print(f'size of variable names is {sys.getsizeof(names)} bytes')

# Print the size of the 'new_list' variable in bytes.
print(f'size of variable new_list is {sys.getsizeof(new_list)} bytes')


## Generator
# A generator is a function that produces or yields a sequence of values 
# using 'yield' method.

# When a generator function is called, it returns a generator object without 
# even beginning execution of the function. When the next( ) method is called
# for the first time, the function starts executing until it reaches the yield 
# statement, which returns the yielded value. The yield keeps track i.e., remembers
# the last execution and the second next( ) call continues from previous value.

# Simple function 
import sys  # Importing the sys module to access system-related information

# Define a function 'squence' that creates a list of numbers from 0 to N-1
def squence(N):
    x = []  # Initialize an empty list
    for i in range(N):  # Loop from 0 to N-1
        x.append(i)  # Append each number to the list
    return x  # Return the list

# Call the 'squence' function with argument 10000 and store the result in the variable 'alist'
alist = squence(1000000)

# Print the list stored in the variable 'alist'
print(alist)

# Define a generator function 'squence' that yields numbers from 0 to N-1
def squence(N):  
    for i in range(N):  # Loop from 0 to N-1
        yield i  # Yield each number

# Call the 'squence' generator function with argument 100000 and store the 
# generator object in the variable 'blist'
blist = squence(1000000)

# Print the generator object stored in the variable 'blist'
print(blist)

# Print the next value from the generator 'blist'
print(next(blist))

# Print the size of the variable 'alist' in bytes
print(f'size of variable new_list is', sys.getsizeof(alist), 'bytes')

# Print the size of the variable 'blist' in bytes
print(f'size of variable new_list is', sys.getsizeof(blist), 'bytes')

# A generator function to generate Fibonacci numbers up to a specified limit 'limit'.
def fib(limit):   
    # Initialize first two Fibonacci Numbers  
    a, b = 0, 1  # Initialize variables 'a' and 'b' to store the first two Fibonacci numbers.
    # One by one yield next Fibonacci Number 
    while a < limit:  # Continue generating Fibonacci numbers until 'a' exceeds the specified limit.
        yield a  # Yield the current Fibonacci number.
        a, b = b, a + b  # Update 'a' and 'b' to calculate the next Fibonacci number.

# Create a generator object by calling the fib() function with argument 5
x = fib(5) 
print(x)  # Print the generator object

# Iterating over the generator object using next() until StopIteration is raised
while True:
    try:
        print(next(x), end = "\n")  # Print the next Fibonacci number
    except StopIteration:  # Catch StopIteration exception
        break  # Break out of the loop

# END of module